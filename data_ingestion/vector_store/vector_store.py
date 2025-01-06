from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from utils.settings import log, read_params
from dotenv import load_dotenv
from typing import List, Dict
import asyncio
import datetime
import os




# Load environment variables from .env file
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY") # Get the Pinecone API Key


class VECTOR_STORE:
    def __init__(self):
        self.config = read_params(field="PINECONE_DB")
        self.INDEX_NAME = self.config.INDEX_NAME # Get the Pinecone index name
        self.PC = Pinecone() # Get the Pinecone Client
    

    def vector_store(self, docs: List[dict], namespace: str, func) -> None:
        """
            This function is responsible for storing the embeddings of the given documents in a vector store.

            Parameters:
                - docs (List[dict]): A list of dictionaries, where each dictionary represents a document. Each document should have the following keys:
                    - source: The source of the document.
                    - file_path: The file path of the document.
                    - board: The board of the document.
                    - language: The language of the document.
                    - class: The class of the document.
                    - subject: The subject of the document.
                    - subject_part: The subject part of the document.
                    - author: The author of the document.
                    - tags: The tags associated with the document.
                    - page: The page number of the document.
                    - total_pages: The total number of pages in the document.
                    - content: The content of the document.

                - namespace (str): The namespace in which the vectors will be stored in the vector store.

                - func (function): A function that takes a document's content as input and returns its embeddings.

            Returns:
            - None: The function does not return any value. It stores the embeddings of the documents in the vector store.
        """
        try:
            # Check Index Present or Not:
            if not self.PC.has_index(name=self.INDEX_NAME):
                log(log_message=f"Index {self.INDEX_NAME} not found in Pinecone") # logs index not found in Pinecone
                return

            # Connect to Pinecone Index:
            PINECONE_INDEX = self.PC.Index(self.INDEX_NAME)

            vector_list = []
            for i, doc in enumerate(docs):
                metadata = {
                    "source": doc["source"] if doc["source"] else "None",
                    "file_path": doc["file_path"] if doc["file_path"] else "None",
                    "board": doc["board"] if doc["board"] else "None",
                    "language": doc["language"] if doc["language"] else "None",
                    "class": doc["class"] if doc["class"] else "None",
                    "subject": doc["subject"] if doc["subject"] else "None",
                    "subject_part": doc["subject_part"] if doc["subject_part"] else "None",
                    "author": doc["author"] if doc["author"] else "None",
                    "tags": doc["tags"] if doc["tags"] else "None",
                    "page": doc["page"] if doc["page"] else "None",
                    "total_pages": doc["total_pages"] if doc["total_pages"] else "None",
                    "content": doc["content"] if doc["content"] else "None",
                    "date": datetime.datetime.now().strftime("%Y-%m-%d"),
                    "time": datetime.datetime.now().strftime("%H:%M:%S")
                }
                id_ = doc["board"] + "_" + doc["language"] + "_" + doc["class"] + "_" + doc["subject"] + "_" + str(doc["subject_part"]) + "_" + str(i) + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                # Call the passed function to get the embeddings
                embeddings = asyncio.run(func(doc["content"]))

                vc = {
                    'id': id_,
                    'values': embeddings,
                    'metadata': metadata
                }
                vector_list.append(vc)

            # Store vectors in Pinecone
            PINECONE_INDEX.upsert(vectors=vector_list, namespace=namespace)
            log(log_message=f"Successfully stored vectors in Pinecone Index: {self.INDEX_NAME}, Namespace: {namespace}") # logs successful storage of vectors in Pinecone

        except Exception as ex:
            log(log_message=f"Error while vectorizing data: {ex}") # logs error while vectorizing data
            raise ex

    


if __name__ == "__main__":
    pass