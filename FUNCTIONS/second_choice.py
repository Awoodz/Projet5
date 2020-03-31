import pandas
import os

import sys
sys.path.insert(1, '/..')

from DATAS.data import *
from FUNCTIONS.helpers import input_checker
from SQL.sql_class import Sql


def second_choice(username, cursor, connection):
    """This function contains what is happening if user choose second choice"""

    saved_list = []
    row_list = []

    cursor.execute(Sql.call_query(username))

    # Appending list with datas from database
    for row in cursor.fetchall():
        row_list = []
        index = 0
        # Used while to avoid repetitions
        while index != 4:
            row_list.append(row[index])
            index = index + 1
        saved_list.append(row_list)

    # If user never saved any substitute
    if saved_list == []:
        os.system('cls')
        print(no_user_sub_txt)
    # Else, displays the substitute in an array
    else:
        os.system('cls')
        print(saved_sub_txt)
        sub_array = pandas.DataFrame(saved_list, columns=array_columns)
        print(sub_array)
        print(license_txt)

    # Press "enter" bring back to main
    input(back_to_main_txt)
