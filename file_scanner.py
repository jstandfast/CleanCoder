import os
import re
import source_file
import constants

class FileScanner:
    def __init__(self, path):
        self.path = path
        self.file_paths = []

    def scan(self):
        self.file_paths = self.get_paths()
        # This can be fleshed out to scan for all source files

    def get_paths(self):
        paths = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                paths.append(os.path.join(root, file))

        return paths

    def get_java_files(self):
        java_files = []
        for root, dirs, files in os.walk(self.path):
            print(path)
            for file in files:
                if file.endswith(constants.JAVA):
                    java_files.append(os.path.join(root, file))
        return java_files