"""Tests for BibTeX citations."""
from unittest import TestCase

from arxiv.document.parse_abs import parse_abs_file_accessor
from arxiv.identifier import Identifier

from tests import path_of_for_test, TestLocalAbsAccessor, ABS_FILES

from browse.formatting.cite import arxiv_bibtex


abs_to_test = \
    ['0705.0001',
     '1108.5926',
     '1902.11195',
     '1902.05884',
     '1307.0001',
     '1307.0584',
     '1307.0101',
     '1307.0010',
     '1310.8286',
     '0806.0920',
     '1501.05201',
     '1501.99999',
     '1501.00002',
     '1501.00001',
     '0704.0667',
     '0704.0997',
     '0704.0169',
     '0704.0476',
     '0704.0510',
     '0704.0050',
     '0704.0244',
     '0704.0236',
     '0704.0394',
     '0704.0349',
     '0704.0428',
     '0704.0844',
     '0704.0751',
     '0704.0652',
     '0704.0393',
     '0704.0903',
     '0704.0327',
     '0704.0232',
     '0704.0764',
     '0704.0105',
     '0704.0906',
     '0704.0392',
     '0704.0233',
     '0704.0060',
     '0704.0713',
     '0704.0091',
     '0704.0850',
     '0704.0679',
     '0704.0712',
     '0704.0026',
     '0704.0792',
     '0704.0745',
     '0704.0292',
     '0704.0910',
     '0704.0664',
     '0704.0115',
     '0704.0749',
     '0704.0611',
     '0704.0690',
     '0704.0612',
     '0704.0279',
     '0704.0405',
     '0704.0180',
     '0704.0741',
     '0704.0603',
     '0704.0998',
     '0704.0760',
     '0704.0647',
     '0704.0787',
     '0704.0121',
     '0704.0332',
     '0704.0281',
     '0704.0817',
     '0704.0314',
     '0704.0639',
     '0704.0170',
     '0704.0703',
     '0704.0632',
     '0704.0155',
     '0704.0819',
     '0704.0829',
     '0704.0434',
     '0704.0458',
     '0704.0478',
     '0704.0582',
     '0704.0083']


class TestCite(TestCase):
    """Test cite."""

    def test_cite(self):
        """Test cite."""
        
        for arxiv_id_str in abs_to_test:        
            cite=arxiv_bibtex(
                parse_abs_file_accessor(
                    TestLocalAbsAccessor(Identifier(arxiv_id_str), latest=True)))
            self.assertIsNotNone(cite)
