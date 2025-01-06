from utils.settings import log, GETEMBEDDING
from data_loading.load import DOCUMENT_LOADER
from data_ingestion.data_processing.preprocessing import DATAPREPROCESSING
from db_operation.mongo import MONGODB_OPERATION
from vector_store.vector_store import VECTOR_STORE
from pathlib import Path
from typing import List, Dict




class DATAINGESTION_PIPELINE:
    def __init__(self):
        self.doc_loader = DOCUMENT_LOADER()
        self.data_preprocessor = DATAPREPROCESSING()
        self.mongo = MONGODB_OPERATION()
        self.vector_store = VECTOR_STORE()
        self.embeddings = GETEMBEDDING() # Get the embeddings from the settings file
    

    def data_ingestion(self, file_path:Path, collection:str, board: str, language: str, cls: str, subject: str, subject_part: int, author: str = "Admin", tags: list = None) -> None:
        try:
            # Make ALL Upper Case letters:
            collection = collection.upper()
            board = board.upper()
            language = language.upper()
            cls = cls.upper()
            subject = subject.upper()
            author = author.upper()
            tags = [tag.upper() for tag in tags] if tags else None


            log(log_message=f"********** Starting data ingestion Process **********\n") # logs starting data ingestion


            # Load the PDF:
            documents = self.doc_loader.load_pdf(file_path=Path(file_path))

            # Preprocess the data:
            preprocessed_data = self.data_preprocessor.preprocess_data(documents=documents, board=board, language=language, cls=cls, subject=subject, subject_part=subject_part, author=author, tags=tags)

            # Upload the data to MongoDB:
            self.mongo.upload_data(data=preprocessed_data, collection=collection)

            # Store the embeddings in the vector store:
            namespace = collection
            self.vector_store.vector_store(docs=preprocessed_data, 
                                           namespace=namespace, 
                                           func=self.embeddings.get_embeddings_from_hf().aembed_query
                                           )
            
            log(log_message=f"\n********** Data ingestion successful for Completed **********") # logs successful data ingestion


        except Exception as ex:
            log(log_message=f"Error in data ingestion: {ex}") # logs error message when unable to ingest data
            raise ex



if __name__ == "__main__":
    pass