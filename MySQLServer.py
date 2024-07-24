import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        mydb = mysql.connector.connect(
            host="localhost",
            user="Ronald",
            password="chisekele07"
        )

        if mydb.is_connected():
            print("Connected to MySQL server")

            # Create a cursor object
            mycursor = mydb.cursor()

            # Execute a query to create the database
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
