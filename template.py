# File Structures 
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# These are folders and files
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html",
]

# How to create

for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object
    filedir, filename = os.path.split(filepath)  # Splits directory and file name

    if filedir.strip():  # Checking if directory is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory { filedir} for the file {filename}")

    if not filepath.exists() or os.path.getsize(filepath) == 0:  # Check if file doesn't exist or empty
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} is already created")
