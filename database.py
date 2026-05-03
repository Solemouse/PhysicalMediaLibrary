import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="PhysicalMedia",
            user="root",
            password="yeetus"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

