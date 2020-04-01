import mysql.connector
import os
from DATAS.data import *
from FUNCTIONS.first_choice import first_choice
from FUNCTIONS.second_choice import second_choice
from FUNCTIONS.helpers import input_checker
from API.api_class import Api
from SQL.sql_class import Sql


def __main__():
    """Execute the program"""

    connection_checker = False
    while not connection_checker :
        # Connection to SQL database
        try:
            connection = mysql.connector.connect(
                host=db_host,
                database=db_database,
                user=db_user,
                password=db_password,
                charset=db_charset,
                use_unicode=True
            )
            if connection.is_connected():
                cursor = connection.cursor()
                connection_checker = True
        # if fail, the database may not exists, the code will create it
        except:
            Sql.database_creation()

    # os.system('cls')

    choice_input = ""

    # Ask the user a "login"
    username = input(username_req_txt)
    if username == "":
        username = default_username
    
    cursor.execute(sql_user_query, (username,))
    connection.commit()

    os.system('cls')

    while choice_input != 3:
        print(main_req_txt)
        # Set/reset choice_input to "" to avoid loop
        choice_input = ""
        # Displaying choices to user - What he want to do.
        for elem in init_choice:
            print(elem)

        # User makes a choice
        while not input_checker(choice_input, init_choice):
            choice_input = input(init_input_txt)

        # If user wants to look for a substitute
        if choice_input == "1":
            first_choice(username, cursor, connection)
            os.system('cls')
        # If user wants to look for his saved substitutes
        elif choice_input == "2":
            second_choice(username, cursor, connection)
            os.system('cls')
        # If user wants to leave the program
        else:
            os.system('cls')
            exit()


__main__()
