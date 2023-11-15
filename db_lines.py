from line_obj import LineObj
from mysql.connector import Error

def check_if_line_exists(db_connection, file_id, line_num, line_text):
	try:
		cursor = db_connection.cursor()
		check_line_sql = "SELECT line_id FROM file_lines WHERE file_id = %s AND line_number = %s AND line_text = %s"
		params = (file_id, line_num, line_text)
		cursor.execute(check_line_sql, params)
		line = cursor.fetchone()
		cursor.close()  # Closing the cursor

		if line:
			return line[0]  # Return the line_id
		else:
			return False

	except mysql.connector.Error as error:
		print(f"Error in check_if_line_exists: {error}")
		return None  # Return None to indicate an error occurred
	finally:
		cursor.close()  # Ensuring the cursor is closed in case of error

def delete_line(db_connection, line_id):
	try:
		cursor = db_connection.cursor()
		delete_line_sql = "DELETE FROM file_lines WHERE line_id = %s;"

		# Executing the command
		cursor.execute(delete_line_sql, (line_id,))

		# Committing the changes to the database
		db_connection.commit()

		print(f"Line with ID {line_id} has been deleted.")

	except mysql.connector.Error as error:
		print(f"Error: {error}")
		db_connection.rollback()  # Rollback in case of error
	finally:
		cursor.close()

def insert_line(db_connection, file_id, line_obj):
	try:
		cursor = db_connection.cursor()
		insert_line_sql = "INSERT INTO file_lines (file_id, line_number, line_text) VALUES (%s, %s, %s)"
		params = (file_id, line_obj.line_num, line_obj.line_text)
		cursor.execute(insert_line_sql, params)

		# Get the ID of the newly inserted line
		line_id = cursor.lastrowid

		# Commit the transaction
		db_connection.commit()

		return line_id

	except mysql.connector.Error as error:
		print(f"Error: {error}")
		db_connection.rollback()  # Rollback in case of error
		return None
	finally:
		cursor.close()  # Closing the cursor
