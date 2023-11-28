# from directory_scanner import DirectoryScanner
# from file_reader import FileReader
# from file_saver import FileSaver
from db_connector import get_db_connection
import db_projects

class ProjectLoader:
	def __init__(self, project_path, project_name):
		self.project_path = project_path
		self.project_name = project_name

	def load_project(self):
		db_connection = get_db_connection()
		project_id = self.store_project(db_connection)
		if project_id:
			file_paths = self.scan_directory()
			files = self.read_files(file_paths)
			self.save_files(db_connection, project_id, files)
		db_connection.close()