import os
import re
from tqdm import tqdm

class DirectoryScanner:
    def __init__(self, path):
        self.path = path
        self.file_paths = []

    def get_file_paths(self):
        return self.file_paths

    def scan(self):
        self.file_paths = self.__scan_file_paths__()

    def __scan_file_paths__(self):
        paths = []
        for root, dirs, files in tqdm(os.walk(self.path), desc="Scanning Directories"):
            for file in files:
                file_path = os.path.join(root, file)
                paths.append(file_path)
        return paths