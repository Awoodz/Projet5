import pandas

from datas import data as Dt
from functions.helpers import list_builder


def second_choice(username, cursor, connection):
    """This function contains what is happening"""
    """if user choose second choice."""

    saved_list = []

    cursor.execute(Dt.SQL_CALL_QUERY, (username,))

    # Appending list with datas from database
    saved_list = list_builder(cursor, 4)

    # If user never saved any substitute
    if saved_list == []:
        print(Dt.NO_USER_SUB_TXT)

    # Else, displays the substitute in an array
    else:
        print(Dt.SAVED_SUB_TXT)
        sub_array = pandas.DataFrame(saved_list, columns=Dt.ARRAY_COLUMNS)
        print(sub_array)
        print(Dt.LICENCE_TXT)

    # Press "enter" bring back to main
    input(Dt.BACK_TO_MAIN_TXT)
