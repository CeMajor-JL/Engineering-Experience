import os
from pathlib import Path

def organize_folder(path: str):
    base_path = Path(path)

    if not base_path.exists():
        print("Path does not exist")
        return

    for file in base_path.iterdir():
        if file.is_file():
            ext = file.suffix[1:] or "no_extension"
            target_dir = base_path / ext

            target_dir.mkdir(exist_ok=True)
            file.rename(target_dir / file.name)

    print("Files organized by extension")

if __name__ == "__main__":
    folder = input("Enter folder path to organize: ").strip()
    organize_folder(folder)