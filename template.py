import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s:')

project_name="TextSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep", 
    f"src/{project_name}/.__init__.py",   
    f"src/{project_name}/components/.__init__.py",   
    f"src/{project_name}/utils/.__init__.py",   
    f"src/{project_name}/utils/common.py",   
    f"src/{project_name}/logging/common.py",   
    f"src/{project_name}/config/common.py",   
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/configuration.py",
    f"src/{project_name}/entity/configuration.py",
    f"src/{project_name}/constant/configuration.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "DockerFile",
    "requirements.txt",
    "setup.py",
    "research/trail.ipynb"    
]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory:{filedir} for filename:{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating file path:{filepath}")
    else:
        logging.info(f"file name already exists: {filename}") 