from line_obj import LineObj
import db_lines

class LineSaver:
	def __init__(self, lines):
		self.lines = lines

	def store_lines(self, db_connection, file_id):

		for line in self.lines:
			existing_id = db_lines.check_if_line_exists(db_connection, file_id, line.line_num, line.line_text)

			if existing_id:
				db_lines.delete_line(db_connection, existing_id)

			db_lines.insert_line(db_connection, file_id, line)
