from file_obj import FileObj
import db_files
from tqdm import tqdm

class FileSaver:
	def __init__(self, files):
		self.files = files
	
	def store_files(self, db_connection, project_id):

		for file in tqdm(self.files, desc="Storing Files"):
			existing_id = db_files.check_if_file_exists(db_connection, project_id, file.file_name, file.file_path)

			if existing_id:
			   db_files.delete_file(db_connection, existing_id)

			db_files.insert_file(db_connection, project_id, file)