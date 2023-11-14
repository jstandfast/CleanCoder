class LineObj:
	def __init__(self, num, text):
		self.line_num = num
		self.line_text = text

	def get_line_num(self):
		return self.line_num

	def get_line_text(self):
		return self.line_text

	def set_line_num(self, num):
		self.line_num = num

	def set_line_text(self, text):
		self.line_text = text

	def __str__(self):
		return f"{self.line_num}: {self.line_text}"