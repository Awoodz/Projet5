import sys

import mysql.connector

from datas import data as Dt
from functions.first_choice import first_choice
from functions.helpers import input_checker
from functions.second_choice import second_choice
from sql.sql_class import Sql


class Main():
    """Execute the program"""

    def __init__(self):
        """Execute the database creation if no database was found"""
        try:
            mysql.connector.connect(
                host=Dt.db_host,
                database=Dt.db_database,
                user=Dt.db_user,
                password=Dt.db_password,
                charset=Dt.db_charset,
                use_unicode=True,
            )
        except mysql.connector.Error as error:
            print(error)
            Sql.database_creation()

    def home_screen(self):
        """Lauch program in terminal"""

        sys.path.insert(1, "/..")
        connection_checker = False
        while not connection_checker:
            # Connection to SQL database
            try:
                connection = mysql.connector.connect(
                    host=Dt.db_host,
                    database=Dt.db_database,
                    user=Dt.db_user,
                    password=Dt.db_password,
                    charset=Dt.db_charset,
                    use_unicode=True,
                )
                if connection.is_connected():
                    cursor = connection.cursor()
                    connection_checker = True
            # if fail, the database may not exists, the code will create it
            except mysql.connector.Error as error:
                print(error)

        choice_input = ""

        # Ask the user a "login"
        username = input(Dt.username_req_txt)
        if username == "":
            username = Dt.default_username

        cursor.execute(Dt.sql_user_query, (username,))
        connection.commit()

        while choice_input != 3:

            # Set/reset choice_input to "" to avoid loop
            choice_input = ""
            # Displaying choices to user - What he want to do.

            # User makes a choice
            while not input_checker(choice_input, Dt.init_choice):
                print(Dt.main_req_txt)
                for elem in Dt.init_choice:
                    print(elem)
                choice_input = input(Dt.init_input_txt)

            # If user wants to look for a substitute
            if choice_input == "1":
                first_choice(username, cursor, connection)
            # If user wants to look for his saved substitutes
            elif choice_input == "2":
                second_choice(username, cursor, connection)
            # If user wants to leave the program
            else:
                exit()


def main():
    """main task"""
    init = Main()
    init.home_screen()


if __name__ == '__main__':
    main()
