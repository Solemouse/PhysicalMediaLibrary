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


def add_location(connection, name, address):
    # Add locations to the database.
    try:
        cursor = connection.cursor()
        query = "INSERT INTO Locations (name, address) VALUES (%s, %s)"
        cursor.execute(query, (name, address))
        connection.commit()
        print(f"Successfully added location {name}.")
    except Error as e:
        print(f"Failed to add location. {e}")


def add_renter(connection, name):
    # Add a renter to the database.
    try:
        cursor = connection.cursor()
        query = "INSERT INTO Renters (name, num_loans) VALUES (%s, 0)"
        cursor.execute(query, (name))
        connection.commit()
        print(f"Successfully added renter {name}.")
    except Error as e:
        print(f"Failed to add renter. {e}")


def add_media_type(connection, type, category):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO Media_Types (type, category) VALUES (%s, %s)"
        cursor.execute(query, (type, category))
        connection.commit()
        print(f"Successfully added media type {type}.")
    except Error as e:
        print(f"Failed to add media type. {e}")


def add_media_name(connection, name, acquiry_Date, quantity, location_id, type_id):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO Media_Names (location_id, name, acquiry_Date, quantity, type_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (location_id, name, acquiry_Date, quantity, type_id))
        connection.commit()
        print(f"Successfully added media {name}.")
    except Error as e:
        print(f"Failed to add media. {e}")


def add_media(connection, media_type_id, media_name_id):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO Media (media_type_id, media_name_id) VALUES (%s, %s)"
        cursor.execute(query, (media_type_id, media_name_id))
        connection.commit()
    except Error as e:
        print(f"Encountered an error. {e}")


def add_loan(connection, renter_id, media_id, check_out_Date, loan_expiration, home_id):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO Active_Loans (renter_id, media_id, check_out_Date, loan_expiration, home_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (renter_id, media_id, check_out_Date, loan_expiration, home_id))
        connection.commit()
        print(f"Successfully added loan for {renter_id} of media {media_id}.")
    except Error as e:
        print(f"Failed to add loan. {e}")
