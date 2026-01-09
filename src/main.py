# src/main.py


from .sorter import categorize_files_by_type, create_folders
from .config import CATEGORY_MAP

def main(base_url: str, out_url:str):
    while True:
        create_all_folders: str = input("Create folders for all categories? (Yes/No) ") # I.e. if create folder for videos etc. though only images exists in folder - Yes
        if create_all_folders == "Yes":
            create_all_folders = True
            break
        elif create_all_folders == "No":
            create_all_folders = False
            break
    
    create_folders(base_url, out_url, CATEGORY_MAP, create_all_folders)
    categorize_files_by_type(base_url, out_url, CATEGORY_MAP)

#main("input", "output")
