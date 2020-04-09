import pandas

from datas.data import Dt
from functions.helpers import list_builder


def second_choice(username, cursor, connection):
    """This function contains what is happening if user choose second choice"""

    saved_list = []

    cursor.execute(Dt.sql_call_query, (username,))

    # Appending list with datas from database
    saved_list = list_builder(cursor, 4)

    # If user never saved any substitute
    if saved_list == []:
        print(Dt.no_user_sub_txt)

    # Else, displays the substitute in an array
    else:
        print(Dt.saved_sub_txt)
        sub_array = pandas.DataFrame(saved_list, columns=Dt.array_columns)
        print(sub_array)
        print(Dt.license_txt)

    # Press "enter" bring back to main
    input(Dt.back_to_main_txt)
