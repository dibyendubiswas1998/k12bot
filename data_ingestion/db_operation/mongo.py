from pymongo import MongoClient
from utils.settings import log, read_params
from dotenv import load_dotenv
from typing import List, Dict
import os



# Load environment variables from .env file
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI") # Get the MongoDB URI




class MONGODB_OPERATION:
    def __init__(self):
        self.config = read_params(field="MONGODB") # read the config.yaml file
        self.URI = MONGODB_URI
        self.DB_NAME = self.config.DB_NAME # Get the MongoDB database name

    def connect(self) -> MongoClient:
        """
            Connects to the MongoDB database using the provided URI.

            Parameters:
                - None

            Returns:
                - MongoClient: A MongoClient object representing the connection to the MongoDB database.

            Raises:
                - Exception: If an error occurs while connecting to the MongoDB database.
        """
        try:
            client = MongoClient(self.URI)
            log(f"Successfully connected to MongoDB: {self.DB_NAME}") # logs successful connection to MongoDB
            return client

        except Exception as ex:
            log(f"Failed to connect to MongoDB: {ex}") # logs error message when unable to connect to MongoDB
            raise ex

        
    def upload_data(self, data: List[dict], collection: str) -> None:
        """
            Uploads data to a specified MongoDB collection.

            Parameters:
                - data (List[dict]): A list of dictionaries representing the data to be uploaded.
                - collection (str): The name of the MongoDB collection to which the data will be uploaded.

            Returns:
                - None: This function does not return any value.

            Raises:
                - Exception: If an error occurs while connecting to the MongoDB database or uploading the data.
        """
        try:
            if not self.collection_exists(collection=collection):
                log(f"Need to creating collection: {collection}") # logs message when creating a new collection
                return

            client = self.connect() # connect to MongoDB
            db = client[self.DB_NAME]
            col = db[collection]
            
            col.insert_many(data) # insert data into MongoDB collection
            client.close() # close the connection to MongoDB

            log(log_message=f"Close MongoDB connection") # logs closing MongoDB connection
            log(f"Successfully uploaded data to MongoDB: {collection}, Size of data: {len(data)}") # logs successful upload of data to MongoDB

        except Exception as ex:
            log(f"Error uploading data to MongoDB: {ex}")
            raise ex

        

    def collection_exists(self, collection: str) -> bool:
        """
            Checks if a specified MongoDB collection exists in the current database.

            Parameters:
                - collection (str): The name of the MongoDB collection to check for existence.

            Returns:
                - bool: True if the collection exists, False otherwise.

            Raises:
                - Exception: If an error occurs while connecting to the MongoDB database.
        """
        try:
            client = self.connect()  # connect to MongoDB
            db = client[self.DB_NAME]
            collections = db.list_collection_names()
            
            client.close()  # close the connection to MongoDB
            log(log_message=f"Close MongoDB connection") # logs closing MongoDB connection

            return collection in collections

        except Exception as ex:
            log(f"Error checking if collection exists: {ex}")  # logs error message when unable to check if collection exists
            raise ex


if __name__ == "__main__":
    pass