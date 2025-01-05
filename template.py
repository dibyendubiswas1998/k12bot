import os
from pathlib import Path
import logging



# Set up basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)


# Project Structure:
project_name = "K12 ChatBot"
list_of_files = [
    ".jenkins/.gitkeep",  # CICD pipeline files.
    ".github/workflows/.gitkeep",
    
    "config/config.yaml", # config/config.yaml file.
    "config/secrect.yaml", # config/secrect.yaml file.
    ".env", # enviroments variables

    "logs/logs.log", # store logs into local directory.
    "cookbooks/.gitkeep", # Store all cookbooks.
    "documents/.gitkeep", # Store all documents related to the project.

    "main.py", # main.py file
    "setup.py", # setup.py file
    "app.py", # app.py file
    "requirements.txt", # requirements.txt file    

    "Dockerfile", # Dockerfile
    "deployment.yaml", # deployment.yaml file for kubernetest
    "services.yaml", # services.yaml file for Kubernetes
]


def create_project_template(project_template_lst):
    """
    Creates directories and files based on the provided file paths.

    Args:
        project_template_lst (list): A list of file paths.

    Returns:
        None

    Raises:
        OSError: If there is an error creating directories or files.
        IOError: If there is an error creating directories or files.
        Exception: If there is an unknown error.

    Example Usage:
        project_template_lst = ['dir1/file1.txt', 'dir2/file2.txt', 'file3.txt']
        create_project_template(project_template_lst)
    """
    try:
        for filepath in project_template_lst:
            filepath = Path(filepath)
            file_dir, file_name = filepath.parent, filepath.name

            if file_dir != "":
                Path(file_dir).mkdir(parents=True, exist_ok=True)
                logging.info(f"Created directory: {file_dir}")

            if (not filepath.exists()) or (filepath.stat().st_size == 0):
                filepath.touch()
                logging.info(f"Created file: {filepath}")
            else:
                logging.info(f"{file_name} already exists")

    except (OSError, IOError) as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"Unknown error: {e}")
        



if __name__ == "__main__":
    logging.info(f"Created project template for: {project_name}")
    create_project_template(list_of_files)