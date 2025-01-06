# Data Ingestion Feature for K12bot



## Overview

The `data_ingestion` feature in the `K12bot` project is responsible for extracting, preprocessing, and ingesting data from various sources into the system. This module handles data cleaning, transformation, and storage, ensuring the chatbot can efficiently utilize accurate and structured information.

## Features

- **Data Extraction**: Load data from multiple sources like PDFs, databases, and APIs.
- **Data Preprocessing**: Clean and transform data by removing unnecessary characters like newlines, tabs, and extra spaces.
- **Storage Integration**: Store preprocessed data in **`MongoDB`** and create embeddings for storage in **`Pinecone`** Vector Database.

## Directory Structure:
### Descriptions

- **`config/config.yml`**: Configuration file containing essential settings for MongoDB, Pinecone, and other integration points.
- **`cookbooks/`**: This directory holds experiments, typically Jupyter notebooks or scripts, for testing and demonstrating the data ingestion process.
- **`data_ingestion/`**: The core package where the main logic for the data ingestion pipeline resides:
  - **`data_loading/`**: Module responsible for fetching data from external sources like PDFs, APIs, or databases.
  - **`data_processing/`**: Contains scripts to clean and transform the raw data into a usable format.
  - **`db_operation/`**: Handles operations related to storing processed data into MongoDB.
  - **`vector_store/`**: Responsible for converting data into vector embeddings and storing them in Pinecone.
- **`utils/`**: Contains utility scripts and helper functions that assist with tasks like logging, configuration reading, or file handling.

This structure provides a clear and organized layout for your data ingestion pipeline, making it easy for developers to navigate and understand the purpose of each component.


## Setup Instructions

1. **Clone the Repository**:
    ```bash
   git clone https://github.com/dibyendubiswas1998/K12bot.git
   cd K12bot
    ```

2. **Checkout the `data_ingestion` Branch:**
    ```bash
        git checkout feature/data_ingestion
    ```

3. **Install Dependencies:** Ensure you have Python 3 and pip installed. Then, install the required packages:
    ```bash
        pip install -r requirements.txt
    ```

4. **Configure `MongoDB` and `Pinecone`:** Update the config/config.yaml file with your MongoDB and Pinecone credentials.



## Development Information:
- **Developer Name:** Dibyendu Biswas
- **Email Id:** dibyendubiswas1998@gmail.com
- **Feature Version:** **`v0.0.1`**
