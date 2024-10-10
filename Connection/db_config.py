import mysql.connector
from mysql.connector import Error


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='10.11.13.118',
            port=3306,
            database='MikV1234_cameranet',
            user='MikV1234_User',
            password='12345'
        )
        print("Подключение к MySQL успешно")
    except Error as e:
        print(f"Произошла ошибка: '{e}'")

    return connection
