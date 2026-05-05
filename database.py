import mysql.connector
from mysql.connector import Error


def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="PhysicalMedia",
            user="root",
            password="password"
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


def add_renter(connection, name, num_loans):
    # Add a renter to the database.
    try:
        cursor = connection.cursor()
        query = "INSERT INTO Renters (name, num_loans) VALUES (%s, %s)"
        cursor.execute(query, (name, num_loans))
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


def pull_data(connection, table):
    try:
        cursor = connection.cursor(buffered=True)
        query = f"SELECT * FROM {table} ORDER BY id"
        cursor.execute(query)
        connection.commit()
        return cursor
    except Error as e:
        print(f"Failed to retrieve data from the database. {e}")
        return None


def update_data(connection, table, row, column, value):
    try:
        cursor = connection.cursor()
        query = f"UPDATE {table} SET {column}=%s WHERE id=%s"
        cursor.execute(query, (value, row))
        connection.commit()
    except Error as e:
        print(f"Failed to update data. {e}")


def get_media_id(connection, name, quantity, location_id):
    try:
        cursor = connection.cursor(buffered=True)
        query = "SELECT id FROM Media_Names WHERE name = %s AND location_id = %s AND quantity = %s"
        cursor.execute(query, (name, location_id, quantity))
        connection.commit()
        return cursor
    except Error as e:
        print(f"Failed to retrieve Media ID. {e}")
        return None


def increment_loan_count(connection, renter_id):
    try:
        cursor = connection.cursor()
        query = "UPDATE Renters SET num_loans = num_loans + %s WHERE id = %s"
        cursor.execute(query, ("1", renter_id))
        connection.commit()
    except Error as e:
        print(f"Failed to increment loan counter. {e}")


def decrement_loan_count(connection, renter_id):
    try:
        cursor = connection.cursor()
        query = "UPDATE Renters SET num_loans = num_loans - %s WHERE id = %s"
        cursor.execute(query, ("1", renter_id))
        connection.commit()
    except Error as e:
        print(f"Failed to decrement loan counter. {e}")


def delete_data(connection, table, row):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM {table} WHERE id = %s OR id = %s"
        cursor.execute(query, (row, row))
        connection.commit()
    except Error as e:
        print(f"Failed to delete data. {e}")


def get_media_type_id(connection, media_name_id):
    try:
        cursor = connection.cursor(buffered=True)
        query = "SELECT type_id FROM Media_Names WHERE id = %s OR id = %s"
        cursor.execute(query, (media_name_id, media_name_id))
        connection.commit()
        return cursor
    except Error as e:
        print(f"Failed to retrieve Media Type ID. {e}")
        return None


def get_media_junct_id(connection, media_name_id, media_type_id):
    try:
        cursor = connection.cursor(buffered=True)
        query = "SELECT id FROM Media WHERE media_name_id = %s AND media_type_id = %s"
        cursor.execute(query, (media_name_id, media_type_id))
        connection.commit()
        return cursor
    except Error as e:
        print(f"Failed to retrieve Media ID. {e}")
        return None


def main():
    print("This is the wrong file. Please run main.py instead.")
    exit(0)


if __name__ == "__main__":
    main()
