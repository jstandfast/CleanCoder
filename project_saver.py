from directory_scanner import DirectoryScanner
from file_reader import FileReader
from file_saver import FileSaver
from db_connector import get_db_connection
import db_projects

class ProjectSaver:
	def __init__(self, project_path, project_name):
		self.project_path = project_path
		self.project_name = project_name

	def save_project(self):
		db_connection = get_db_connection()
		project_id = self.store_project(db_connection)
		if project_id:
			file_paths = self.scan_directory()
			files = self.read_files(file_paths)
			self.save_files(db_connection, project_id, files)
		db_connection.close()

	def scan_directory(self):
		scanner = DirectoryScanner(self.project_path)
		scanner.scan()
		return scanner.get_file_paths()

	def read_files(self, file_paths):
		reader = FileReader(file_paths)
		reader.read()
		return reader.file_objs

	def save_files(self, db_connection, project_id, files):
		saver = FileSaver(files)
		saver.store_files(db_connection, project_id)

	def store_project(self, db_connection):
		existing_id = db_projects.check_if_project_exists(db_connection, self.project_name, self.project_path)

		if existing_id:
			proceed = input("Project already exists. Do you want to overwrite (y/n)? ")
			if proceed.lower() == 'y':
				db_projects.delete_project(db_connection, existing_id)
			else:
				return False

		new_id = db_projects.insert_project(db_connection, self.project_name, self.project_path)

		if new_id:
			return new_id
		else:
			print("New project not stored in the database.")
			return False