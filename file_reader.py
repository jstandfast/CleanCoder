from file_obj import FileObj
from line_obj import LineObj
import constants

class FileReader:
	def __init__(self, file_paths):
		self.file_paths = file_paths
		self.file_objs = []

	def read(self):
		self.file_objs = [self.read_file(path) for path in self.file_paths]

	def read_file(self, path):
		print(f"Working on path: {path}")
		name = path.rsplit('\\')[-1] if path is not None else None
		lang = name.rsplit('.')[-1] if name is not None else None
		line_objs = []

		# Will add functionality for all retrievable file types in future.
		if lang == constants.JAVA: 
			with open(path, 'r') as file:
				lines = file.readlines()
				for num, text in enumerate(lines, start=1):
					line_obj = LineObj(num, text)
					line_objs.append(line_obj)

		return FileObj(path, name, lang, line_objs)