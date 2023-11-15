import mysql.connector
from db_config import db_config

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        print("Successfully connected to database.")
        return connection
    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL: {error}")
        return None