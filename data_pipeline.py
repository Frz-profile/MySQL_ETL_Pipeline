#pip install mysql-connector-python
#pip install pandas sqlalchemy

import mysql.connector
import pandas as pd

def createDatabase():
    # Establish the connection
    conn = mysql.connector.connect(
        host="localhost",   # Change if using a remote MySQL server ---------------------
        user="root",        # Replace with your MySQL username --------------------------
        password=""  # Replace with your MySQL password ---------------------------------
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Create a database
    database_name = "ETL_Project_DB"
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

    print(f"Database '{database_name}' created successfully!")

    # Close the connection
    cursor.close()
    conn.close()

def createTableSQL():
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",   # Change to your host ---------------------------------------
        user="root",         # Change to your MySQL username ----------------------------
        password="",  # Change to your MySQL password -----------------------------------
        database="ETL_Project_DB"  # Change to your MySQL database name -----------------
    )

    cursor = conn.cursor()

    # Create the 'users' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT,
            country VARCHAR(100)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Table 'users' created successfully!")

def inputDatabaseData():
    # Database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",         # Change to your MySQL username ----------------------------
        password="",  # Change to your MySQL password -----------------------------------
        database="ETL_Project_DB"  # Change to your database name -----------------------
    )

    cursor = conn.cursor()

    # Load CSV file into a DataFrame
    csv_file = r"C:\Users\data.csv" # Choose your path ----------------------------------
    df = pd.read_csv(csv_file)

    # Define the table name
    table_name = "users"

    # Insert data row by row
    for _, row in df.iterrows():
        sql = f"INSERT INTO {table_name} (name, age, country) VALUES (%s, %s, %s)"
        values = (row["Name"],row["Age"],row["Country"])
        cursor.execute(sql, values)

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

    print(f"Data from {csv_file} imported successfully into {table_name}!")

createDatabase()
createTableSQL()
inputDatabaseData()