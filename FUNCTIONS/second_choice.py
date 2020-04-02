import pandas
import os
import sys

sys.path.insert(1, '/..')

from DATAS.data import *
from FUNCTIONS.helpers import input_checker
from FUNCTIONS.helpers import list_builder


def second_choice(username, cursor, connection):
    """This function contains what is happening if user choose second choice"""

    saved_list = []

    cursor.execute(sql_call_query, (username,))

    # Appending list with datas from database
    saved_list = list_builder(cursor, 4)

    # If user never saved any substitute
    if saved_list == []:

        print(no_user_sub_txt)
    # Else, displays the substitute in an array
    else:

        print(saved_sub_txt)
        sub_array = pandas.DataFrame(saved_list, columns=array_columns)
        print(sub_array)
        print(license_txt)

    # Press "enter" bring back to main
    input(back_to_main_txt)
