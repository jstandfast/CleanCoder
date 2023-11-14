from directory_scanner import DirectoryScanner
from file_reader import FileReader
from file_saver import FileSaver

class ProjectSaver:
	def __init__(self, project_path, project_name):
		self.project_path = project_path
		self.project_name = project_name

	def save_project(self):
		file_paths = scan_directory
		files = read_files
		save_files(files)

	def scan_directory(self):
		scanner = DirectoryScanner(self.project_path)
		scanner.scan()
		return scanner.get_file_paths()

	def read_files(self):
		reader = FileReader(files)
		reader.read()
		return reader.get_file_objects()

	def save_files(self, files):
		saver = FileSaver(files)
		saver.store_files()