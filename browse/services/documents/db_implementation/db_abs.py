"""Legacy DB backed core metadata service."""
from typing import Dict, List, Optional

from browse.domain.metadata import DocMetadata
from browse.domain.identifier import Identifier
from browse.services.documents.config.deleted_papers import DELETED_PAPERS

from browse.services.documents.base_documents import DocMetadataService, \
    AbsDeletedException, AbsNotFoundException 

from browse.services.database.models import Metadata

from .convert import to_docmeta


class DbDocMetadataService(DocMetadataService):
    """Class for arXiv document metadata service."""

    
    def __init__(self,
                 db) -> None:
        """Initialize the DB document metadata service."""
        self.db = db

    
    def get_abs(self, arxiv_id: str) -> DocMetadata:
        """Get the .abs metadata for the specified arXiv paper identifier.

        Parameters
        ----------
        arxiv_id : str
            The arXiv identifier string.

        Returns
        -------
        :class:`DocMetadata`
        """
        paper_id = Identifier(arxiv_id=arxiv_id)
        if paper_id.id in DELETED_PAPERS:
            raise AbsDeletedException(DELETED_PAPERS[paper_id.id])

        latest_version = self._abs_for_version(identifier=paper_id)
        return latest_version

        #TODO deal with versions
        # if not paper_id.has_version \
        #    or paper_id.version == latest_version.version:
        #     return dataclasses.replace(latest_version,
        #                                is_definitive=True,
        #                                is_latest=True)

        # try:
        #     this_version = self._abs_for_version(identifier=paper_id,
        #                                          version=paper_id.version)
        # except AbsNotFoundException as e:
        #     if paper_id.is_old_id:
        #         raise

        #     raise AbsVersionNotFoundException(e) from e

        # Several fields need to reflect the latest version's data
        # combined_version: DocMetadata = dataclasses.replace(
        #     this_version,
        #     version_history=latest_version.version_history,
        #     categories=latest_version.categories,
        #     primary_category=latest_version.primary_category,
        #     secondary_categories=latest_version.secondary_categories,
        #     primary_archive=latest_version.primary_archive,
        #     primary_group=latest_version.primary_group,
        #     is_definitive=True,
        #     is_latest=False)

        # return combined_version


    def _abs_for_version(self, identifier: Identifier,
                         version: Optional[int] = None) -> DocMetadata:
        res = Metadata.query.filter( Metadata.paper_id.like( identifier.id ) ).first()
        if not res:
            raise AbsNotFoundException()
        return to_docmeta(res)
    
    def get_dissemination_formats(self,
                                  docmeta: DocMetadata,
                                  format_pref: Optional[str] = None,
                                  add_sciencewise: bool = False) -> List[str]:
        """Get a list of formats that can be disseminated for this DocMetadata.

        Several checks are performed to determine available dissemination
        formats:
            1. a check for source files with specific, valid file name
               extensions (i.e. for a subset of the allowed source file name
               extensions, the dissemintation formats are predictable)
            2. if formats cannot be inferred from the source file, inspect the
               source type in the document metadata.

        Format names are strings. These include 'src', 'pdf', 'ps', 'html',
        'pdfonly', 'other', 'dvi', 'ps(400)', 'ps(600)', 'nops'.

        Parameters
        ----------
        docmeta : :class:`DocMetadata`
        format_pref : str
            The format preference string.
        add_sciencewise : bool
            Specify whether to include 'sciencewise_pdf' format in list.

        Returns
        -------
        List[str]
            A list of format strings.
        """
        return []


    def get_ancillary_files(self, docmeta: DocMetadata) \
            -> List[Dict]:
        """Get list of ancillary file names and sizes."""
        return []
