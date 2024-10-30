import mysql.connector
from mysql.connector import Error

def insert_into_table(host, database, user, password, table, data):
    connection = None  # Initialize connection variable
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=3306  # Ensure the port is correctly specified
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the insert query
            placeholders = ", ".join(["%s"] * len(data))
            columns = ", ".join(data.keys())
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

            # Execute the insert query
            cursor.execute(query, list(data.values()))
            connection.commit()

            print(f"Inserted {cursor.rowcount} row(s) into {table}")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")