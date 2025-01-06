from langchain_core.documents import Document
from utils.settings import log
from typing import List, Dict
import datetime
import re


class DATAPREPROCESSING:
    def __init__(self):
        pass
    
    def clean_text(self, text:str) -> str:
        try:
            # Remove newlines, tabs, and extra spaces
            text = re.sub(r'[\n\t\r]+', ' ', text)
            text = re.sub(r'\s+', ' ', text)
            return text.strip()

        except Exception as ex:
            log(log_message=f"Error in cleaning text: {ex}")
            raise ex

    def preprocess_data(self, documents: Document, board: str, language: str, cls: str, subject: str, subject_part: int, author: str = "Admin", tags: list = None) -> List[Dict]:
        """
            Preprocess a list of documents by cleaning their content and structuring them.

            Parameters:
                - documents (Document): A list of documents to preprocess.
                - board (str): The board or educational institution associated with the documents.
                - language (str): The language of the documents.
                - cls (str): The class or grade level associated with the documents.
                - subject (str): The subject or topic of the documents.
                - subject_part (int): The specific part or section of the subject.
                - author (str, optional): The author of the documents. Defaults to "Admin".
                - tags (list, optional): A list of tags associated with the documents. Defaults to None.

            Returns:
                - List[Dict]: A list of dictionaries, where each dictionary represents a preprocessed document.
        """
        try:
            processed_docs = []
            for doc in documents:
                # Clean the page content
                cleaned_content = self.clean_text(text=doc.page_content)

                # Create Structured Documents:
                processed_doc = {
                    "source": doc.metadata.get('source', ''),
                    "file_path": doc.metadata.get('file_path', ''),
                    "board": board,
                    "language": language,
                    "class": cls,
                    "subject": subject,
                    "subject_part": subject_part,
                    "author": author,
                    "tags": tags,
                    "page": doc.metadata.get('page', 0),
                    "total_pages": doc.metadata.get('total_pages', 0),
                    "content": cleaned_content,
                    "date": datetime.datetime.now().strftime("%Y-%m-%d"),
                    "time": datetime.datetime.now().strftime("%H:%M:%S")
                }

                
                processed_docs.append(processed_doc)

            log(log_message=f"Successfully preprocessed the data") # logs successful preprocessing of data
            return processed_docs

        except Exception as ex:
            log(log_message=f"Error in preprocessing data: {ex}") # logs error in preprocessing data
            raise ex



if __name__ == "__main__":
    pass