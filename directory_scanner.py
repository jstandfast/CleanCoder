import os
import re

class DirectoryScanner:
    def __init__(self, path):
        self.path = path
        self.file_paths = []

    def get_file_paths(self):
        return self.file_paths

    def scan(self):
        self.file_paths = self.__scan_file_paths__()
        # This can be fleshed out to scan for all source files

    def __scan_file_paths__(self):
        paths = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                paths.append(os.path.join(root, file))
        return paths