from langchain_core.documents import Document
from langchain_community.document_loaders import PDFPlumberLoader, PyPDFium2Loader
from utils.settings import log
from pathlib import Path
import os



class DOCUMENT_LOADER:
    def __init__(self):
        pass

    def load_pdf(self, file_path: Path) -> Document:
        """
            Load a PDF document into a LangChain Document object.

            Parameters:
                - file_path (Path): The path to the PDF file to be loaded.

            Returns:
                Document: A LangChain Document object containing the loaded PDF content.

            Raises:
                Exception: If an error occurs while loading the PDF.
        """
        try:
            loader = PDFPlumberLoader(file_path=file_path)
            documents = loader.load()

            log(log_message=f'Loaded {len(documents)} documents from {file_path}') # log successfully load all documents
            return documents

        except Exception as ex:
            log('logs/load.log', f'Error loading pdf: {ex}') # log error loading pdf
            raise ex


if __name__ == "__main__":
    pass