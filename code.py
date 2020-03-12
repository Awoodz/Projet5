import mysql.connector
import pandas
import os
from DATAS.data import *
from DATAS.first_choice import *
from DATAS.second_choice import *
from DATAS.helpers import input_checker
from API.api_class import *
from SQL.sql_class import *

def main() :

    connection_checker = False
    while connection_checker == False :
        # Connection to SQL database
        try :
            connection = mysql.connector.connect (
                host = 'localhost',
                database = 'P5',
                user = 'testeur',
                password = 'openclassrooms',
                charset = 'utf8mb4',
                use_unicode = True
                )
            if connection.is_connected():
                cursor = connection.cursor()
                connection_checker = True
        # if fail, the database may not exists, the code will create it
        except :
            Sql.database_creation()

    os.system('cls')

    choice_input = ""

    # Ask the user a "login"
    username = input("Entrez un nom d'utilisateur (facultatif) : ")
    if username == "":
        username = "all"

    os.system('cls')
    
    while choice_input !=3 :
        print("Que voulez vous faire ?")
        choice_input = ""
        # Displaying choices to user - What he want to do.
        for elem in init_choice :
            print(elem)

        # User makes a choice
        while input_checker(choice_input, init_choice) == False :
            choice_input = input(init_input_txt)

        # If user wants to look for a substitute
        if choice_input == "1" :
            first_choice(username, cursor, connection)
            # os.system('cls')
        # If user wants to look for his saved substitutes
        elif choice_input == "2" :
            second_choice(username, cursor, connection)
            os.system('cls')
        # If user wants to leave the program
        else :
            os.system('cls')
            exit()

main()

            

            
