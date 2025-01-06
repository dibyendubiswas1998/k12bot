import os
import shutil
import json
import yaml
import time
import logging
from pathlib import Path
from typing import List
from box.exceptions import BoxValueError
from box import ConfigBox
from ensure import ensure_annotations
from typing import Any
from datetime import datetime
from langchain_huggingface import HuggingFaceEmbeddings
from pymongo import MongoClient
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from dotenv import load_dotenv
import asyncio



# Load environment variables from .env file
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN") # Get the HF Toke
MONGODB_URI = os.getenv("MONGODB_URI") # Get the MongoDB URI
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY") # Get the Pinecone API Key



def log(log_message:str, file_object:Path=Path("logs/logs.log")) -> None:
    """
        Logs a message to a file using the Python logging module.

        Args:
            file_object (str): The name of the file to log the message to.
            log_message (str): The message to be logged.

        Raises:
            ValueError: If file_object or log_message is None or empty.

        Returns:
            None
    """
    if not file_object or not log_message:
        raise ValueError('file_object and log_message cannot be None or empty')
    try:
        now = datetime.now()
        date = now.date()
        current_time = now.strftime("%H:%M:%S")
        
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger()

        file_handler = logging.FileHandler(filename=file_object)
        logger.addHandler(file_handler)
        logging.info(f'{date}\t{current_time}\t{log_message}')
        
    except Exception as e:
        raise e


@ensure_annotations
def read_params(field:str=None, config_path:Path=Path("config/config.yaml")) -> ConfigBox:
    """
        Read the YAML file at the specified path and return its contents as a dictionary.

        Args:
            config_path (str): The path to the YAML file.

        Returns:
            ConfigBox: ConfigBox type

        Raises:
            Exception: If there is an error while reading the file.
    """
    try:
        with open(config_path) as yaml_file:
            config = yaml.safe_load(yaml_file)
        
        if field:
            return ConfigBox(config[field])
        else:
           return ConfigBox(config)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as ex:
        raise ex



class GETEMBEDDING:
    def __init__(self):
        self.config = read_params(field="EMBEDDINGS") # read the config.yaml file
        self.__hfem = self.config.HF_MODEL.EMBEDDINGS # Get the HuggingFace model name
    
    
    async def load_embeddings_from_hf(self, query:str) -> List[float]:
        """
            Asynchronously loads embeddings from a specified HuggingFace model for a given query.

            Parameters:
                - query (str): The input text for which embeddings need to be generated.

            Returns:
                - List[float]: A list of float values representing the embeddings of the input query.
            
            Raises:
                - Exception: If an error occurs while loading or generating embeddings.
        """
        try:
            embeddings = HuggingFaceEmbeddings(model_name=self.__hfem)
            log(f"Successfully loaded embeddings from HuggingFace model: {self.__hfem}") # logs successful loading of embeddings from HuggingFace model
            embeddings_result = await embeddings.aembed_query(query)
            return embeddings_result

        except Exception as ex:
            log(f"Error loading embeddings: {ex}") # logs error loading embeddings
            raise ex



class MONGODB:
    def __init__(self):
        self.config = read_params(field="MONGODB") # read the config.yaml file
        self.URI = MONGODB_URI
        self.DB_NAME = self.config.DB_NAME # Get the MongoDB database name

    
class PINECONE:
    def __init__(self):
        self.config = read_params(field="PINECONE")
        self.config.INDEX_NAME = self.config.INDEX_NAME # Get the Pinecone index name
        self.PC = Pinecone() # Get the Pinecone Client




if __name__ == "__main__":
    pass