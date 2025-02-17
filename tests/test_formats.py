"""Tests for formats logic."""

from unittest import TestCase

from arxiv.formats import formats_from_source_flag, formats_from_source_file_name


class TestFormats(TestCase):
    """Tests for formats logic."""

    def test_formats_from_source_file_name(self):
        """Test formats returned from file name."""
        self.assertListEqual(formats_from_source_file_name('foo.pdf'),
                             ['pdfonly'])
        self.assertListEqual(formats_from_source_file_name('/bar.ps.gz'),
                             ['pdf', 'ps'])
        self.assertListEqual(formats_from_source_file_name('abc.html.gz'),
                             ['html'])
        self.assertListEqual(formats_from_source_file_name('baz.html'),
                             [])
        self.assertListEqual(formats_from_source_file_name(''),
                             [])

    def test_formats_from_source_type(self):
        """Tests formats based on metadata source type and other parameters."""
        self.assertListEqual(formats_from_source_flag('I'), ['src'])
        self.assertListEqual(formats_from_source_flag('IS'), [])
        self.assertListEqual(formats_from_source_flag(''),
                             ['pdf', 'ps', 'src', 'other'])
        self.assertListEqual(formats_from_source_flag('P'),
                             ['pdf', 'ps', 'other'])
        self.assertListEqual(formats_from_source_flag('D'),
                             ['pdf', 'src', 'other'])
        self.assertListEqual(formats_from_source_flag('F'),
                             ['pdf', 'other'])
        self.assertListEqual(formats_from_source_flag('H'),
                             ['html', 'other'])
        self.assertListEqual(formats_from_source_flag('X'),
                             ['pdf', 'other'])


def test_format_headers(client_with_test_fs):
    client=client_with_test_fs

    rv=client.head("/format/1601.04345")
    head=rv.headers["Surrogate-Key"]
    assert " format " in " "+head+" "
    assert "format-unversioned" in head
    assert "format-versioned" not in head
    assert "paper-id-1601.04345" in head

    rv=client.head("/format/1601.04345v2")
    head=rv.headers["Surrogate-Key"]
    assert " format " in " "+head+" "
    assert "format-unversioned" not in head
    assert "format-versioned" in head
    assert "paper-id-1601.04345" in head