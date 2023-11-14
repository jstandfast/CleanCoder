class FileSaver:
    def __init__(self, files):
        self.files = files
        for file in self.files:
            print(f"{str(file)}")