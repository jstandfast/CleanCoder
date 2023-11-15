from file_obj import FileObj
from line_obj import LineObj
from line_saver import LineSaver
from mysql.connector import Error

def check_if_file_exists(db_connection, project_id, file_path, file_name):
	try:
		cursor = db_connection.cursor()
		check_file_sql = "SELECT file_id FROM source_files WHERE project_id = %s AND file_path = %s AND file_name = %s"
		params = (project_id, file_path, file_name)
		cursor.execute(check_file_sql, params)
		file = cursor.fetchone()
		cursor.close()  # Closing the cursor

		if file:
			return file[0]  # Return the file_id
		else:
			return False

	except mysql.connector.Error as error:
		print(f"Error in check_if_file_exists: {error}")
		return None  # Return None to indicate an error occurred
	finally:
		cursor.close()  # Ensuring the cursor is closed in case of error

def delete_file(db_connection, file_id):
	try:
		cursor = db_connection.cursor()

		# SQL command to delete lines associated with the file
		delete_lines_sql = "DELETE FROM file_lines WHERE file_id = %s;"

		# SQL command to delete the file
		delete_file_sql = "DELETE FROM source_files WHERE file_id = %s;"

		# Executing the commands
		cursor.execute(delete_lines_sql, (file_id,))
		cursor.execute(delete_file_sql, (file_id,))

		# Committing the changes to the database
		db_connection.commit()

		print(f"File with ID {file_id} and all associated lines have been deleted.")

	except mysql.connector.Error as error:
		print(f"Error: {error}")
		db_connection.rollback()  # Rollback in case of error
	finally:
		cursor.close()

def insert_file(db_connection, project_id, file_obj):
	try:
		cursor = db_connection.cursor()
		insert_file_sql = "INSERT INTO source_files (project_id, file_path, file_name, file_lang) VALUES (%s, %s, %s, %s)"
		params = (project_id, file_obj.file_path, file_obj.file_name, file_obj.file_lang)
		cursor.execute(insert_file_sql, params)

		# Get the ID of the newly inserted file
		file_id = cursor.lastrowid

		# Optionally, insert the lines associated with this file
		# (This part assumes you have a function to insert lines)
		if file_obj.file_lines:
			store_lines = LineSaver(file_obj.file_lines)
			store_lines.store_lines(db_connection, file_id)

		# Commit the transaction
		db_connection.commit()

		return file_id

	except mysql.connector.Error as error:
		print(f"Error: {error}")
		db_connection.rollback()  # Rollback in case of error
		return None
	finally:
		cursor.close()  # Closing the cursor
