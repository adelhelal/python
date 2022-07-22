from pathlib import Path

def file_exists():
    file = Path("models/person.py")
    return file.exists()

def file_list():
    path = Path()
    for file in path.glob("*.*"):
        print(file)

def folder_create():
    folder = Path("resources")
    if not folder.exists():
        folder.mkdir()
