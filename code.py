import mysql.connector
from mysql.connector import Error

from data import *
from code_class import *

for elem in init_choice :
    print(elem)

print(init_answer[input_checker(init_choice) - 1])


# TEST CONNEXION MYSQL

try :
    connection = mysql.connector.connect (
        host = 'localhost',
        database = 'testP5',
        user = 'testeur',
        password = 'openclassrooms'
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connecté au serveur MySQL", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Vous êtes connecté à la base de donnée ", record)

except Error as e:
    print("Une erreur est survenue, ", e)
finally :
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("Fini")        