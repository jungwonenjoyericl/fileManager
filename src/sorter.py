# src/sorter.py

import os
from shutil import rmtree, copy2
from .config import UNKNOWN_FOLDER

def create_folders(base_dir: str, out_dir: str, folders: dict, include_all_folders: bool):

    def reset_output(output): # For testing stages
        for name in os.listdir(output):
            full = os.path.join(output, name)
            if os.path.isdir(full):
                rmtree(full)
    
    #reset_output(out_dir) # Uncomment to reset output folder

    if include_all_folders:
        for folder in folders:
            folder_path = os.path.join(out_dir, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        os.makedirs(os.path.join(out_dir, UNKNOWN_FOLDER))        
    else:
        for filename in os.listdir(base_dir):
            extension = "." + filename.split(".")[-1]
            for folder in folders:
                folder_path = os.path.join(out_dir, folder)
                if extension in folders[folder]:
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    break
        folder_path = os.path.join(out_dir, UNKNOWN_FOLDER)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


def categorize_files_by_type(base_dir: str, out_dir: str, folders: dict):
    for filename in os.listdir(base_dir):
        extension = "." + filename.split(".")[-1]
        file_path = os.path.join(base_dir, filename)
        folder_path = os.path.join(out_dir, UNKNOWN_FOLDER)
        for folder in folders:
            if extension in folders[folder]:
                folder_path  = os.path.join(out_dir, folder)
                break
        copy2(file_path, folder_path)