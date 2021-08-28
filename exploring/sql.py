#testing basic database query using python SQL
import mysql.connector

def main():
    print("basic database query using python SQL")
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
    )

    # mycursor = bd.cursor()

    # mycursor.execute("CREATE DATABASE testdatabase")


if __name__ == "__main__":
    main()