from mysql.connector import Error

def check_if_project_exists(db_connection, project_name, project_path):
	try:
		cursor = db_connection.cursor()
		check_project_sql = "SELECT project_id FROM projects WHERE project_name = %s AND project_path = %s"
		params = (project_name, project_path)
		cursor.execute(check_project_sql, params)
		project = cursor.fetchone()
		cursor.close()  # Closing the cursor

		if project:
			return project[0]  # Return the project_id
		else:
			return False

	except mysql.connector.Error as error:
		print(f"Error in check_if_project_exists: {error}")
		return None  # Return None to indicate an error occurred
	finally:
		cursor.close()  # Ensuring the cursor is closed in case of error


def delete_project(db_connection, project_id):
	try:
		cursor = db_connection.cursor()

		# SQL command to delete lines associated with files of the project
		delete_lines_sql = """
			DELETE FROM file_lines
			WHERE file_id IN (
			SELECT file_id
			FROM source_files
			WHERE project_id = %s
		);
		"""

		# SQL command to delete files associated with the project
		delete_files_sql = "DELETE FROM source_files WHERE project_id = %s;"

		# SQL command to delete the project
		delete_project_sql = "DELETE FROM projects WHERE project_id = %s;"

		# Executing the commands
		cursor.execute(delete_lines_sql, (project_id,))
		cursor.execute(delete_files_sql, (project_id,))
		cursor.execute(delete_project_sql, (project_id,))

		# Committing the changes to the database
		db_connection.commit()

		print(f"Project with ID {project_id} and all associated files have been deleted.")

	except mysql.connector.Error as error:
		print(f"Error: {error}")
		db_connection.rollback()  # Rollback in case of error
	finally:
		cursor.close()

def insert_project(db_connection, project_name, project_path):
	try:
		cursor = db_connection.cursor()
		insert_project_sql = "INSERT INTO projects (project_name, project_path) VALUES (%s, %s)"
		params = (project_name, project_path)
		cursor.execute(insert_project_sql, params)

		# Get the ID of the newly inserted project
		project_id = cursor.lastrowid

		# Commit the transaction
		db_connection.commit()

		return project_id

	except mysql.connector.Error as error:
		print(f"Error: {error}")
		db_connection.rollback()  # Rollback in case of error
		return None
	finally:
		cursor.close()  # Closing the cursor

