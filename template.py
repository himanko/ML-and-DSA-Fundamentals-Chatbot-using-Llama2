import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "ML-and-DSA-chatbot"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/helper.py",
    f"src/{project_name}/config/prompt.py",
    f"src/{project_name}/data/readme.txt",
    f"src/{project_name}/model/instruction.txt",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    ".env",
    "config/config.yaml",
    "dvc.yaml",
    "requirements.txt",
    "app.py",
    "setup.py",
    "research/trails.ipynb",
    "static/.gitkeep",
    "templates/chat.html"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
                     
                     
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty File: {filepath}")
        
            
    else:
        logging.info(f"{filename} is already exist.")
                    