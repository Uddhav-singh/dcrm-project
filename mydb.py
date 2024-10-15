
# these commented lines are from youtube 
# =======================================================
# import mysql.connector

# dataBase = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = 'rootpassword'
# )

# # prepare a cursor objetc 
# cursorObject = dataBase.cursor()

# # Create database 
# cursorObject.execute("CREATE DATABASE elderco")

# print("all done!")

# ==========================================================


import mysql.connector


dataBase = None  # Initialize dataBase to None in case connection fails

try:
    # Establishing a connection to MySQL
    dataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='rootpassword',
        auth_plugin='mysql_native_password'  # Specify the authentication plugin
    )

    # Creating a cursor object to interact with the database
    cursorObject = dataBase.cursor()

    # Creating a new database
    cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

    print("Database 'elderco' created or already exists.")
    
    # Optionally, you can verify if the connection is working by listing databases
    cursorObject.execute("SHOW DATABASES LIKE 'elderco'")
    
    for db in cursorObject:
        print(db)

except mysql.connector.Error as err:
    # Error handling
    print(f"Error: {err}")

finally:
    # Closing the database connection
    if dataBase is not None and dataBase.is_connected():
        cursorObject.close()
        dataBase.close()
        print("MySQL connection is closed")
