class FileObj:
	def __init__(self, path=None, name=None, lang=None, lines=[]):
		self.file_path = path
		self.file_name = name
		self.file_lang = lang
		self.file_lines = lines

	def get_file_path(self):
		return self.file_path

	def get_file_name(self):
		return self.file_name

	def get_file_lang(self):
		return self.file_lang

	def get_file_lines(self):
		return self.file_lines

	def set_file_path(self, path):
		self.file_path = path

	def set_file_name(self, name):
		self.file_name = name

	def set_file_lang(self, lang):
		self.file_lang = lang

	def set_file_lines(self, lines):
		self.file_lines = lines

	def __str__(self):
		file_str = [f"File Name: {self.file_name}\n",
					f"File Path: {self.file_path}\n"] + \
					[str(line) for line in self.file_lines]

		return ''.join(file_str)