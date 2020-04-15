import pandas

from datas import data as Dt
from functions.helpers import input_checker
from functions.helpers import list_builder


def first_choice(username, cursor, connection):
    """This function contains what is happening if user choose first choice."""

    sub_list = []
    cat_list = []
    prod_list = []
    prod_score = []
    cat_input = ""
    prod_input = ""
    sub_input = ""
    choice_input = ""

    # Searching categories in database
    cursor.execute(Dt.SQL_CAT_QUERY)

    # Appending category list with datas from database
    for row in cursor.fetchall():
        cat_list.append(row[0])

    # As long as user's input is not valid :
    while not input_checker(cat_input, cat_list):
        # Display list title (category)
        print(Dt.CAT_LIST_TXT)
        # Display the category list
        for elem in cat_list:
            print(str(cat_list.index(elem) + 1) + " : " + elem)
        # Ask for an user input
        cat_input = input(Dt.CAT_INPUT_TXT)

    # Searching products affiliated to categories in database
    cat_name = cat_list[int(cat_input) - 1]
    print(cat_name)
    cursor.execute(Dt.SQL_PROD_QUERY, (cat_name,))

    # Appending product list with datas from database
    for row in cursor.fetchall():
        prod_list.append(row[0])

    # As long as user's input is not valid :
    while not input_checker(prod_input, prod_list):
        # Display list title (product)
        print(Dt.PROD_LIST_TXT)
        # Display the product list
        for elem in prod_list:
            print(str(prod_list.index(elem) + 1) + " : " + elem)
        # Ask for an user input
        prod_input = input(Dt.PROD_INPUT_TXT)

    # Getting the chosen product's score and category
    prod_name = prod_list[int(prod_input) - 1]
    cursor.execute(Dt.SQL_PROD_SC_QUERY, (prod_name,))

    # Building a list with score and category
    prod_score = list_builder(cursor, 2)
    # Searching for product from the same category with better score
    cursor.execute(Dt.SQL_SUB_QUERY, (prod_score[0][0], prod_score[0][1]))

    # Building list with healthier products as substitutes
    sub_list = list_builder(cursor, 4)
    # Displaying the substitutes
    sub_array = pandas.DataFrame(
        sub_list, columns=Dt.ARRAY_COLUMNS, index=Dt.ARRAY_LINES
    )

    print(sub_array)
    print(Dt.LICENCE_TXT)

    # As long as user's input is not valid :
    while not input_checker(choice_input, Dt.CHOICE_LIST):
        print(Dt.MAIN_REQ_TXT)
        for elem in Dt.CHOICE_LIST:
            print(elem)
        choice_input = input(Dt.INIT_INPUT_TXT)

    if choice_input == "1":

        # User has to pick a substitute to save
        while not input_checker(sub_input, sub_list):
            print(sub_array)
            print(Dt.LICENCE_TXT)
            sub_input = input(Dt.SUB_SAVE_TXT)

        # Getting the name of the selected substitute
        prod_name = sub_list[int(sub_input) - 1][0]

        # Getting the product id in MySQL Products table
        cursor.execute(Dt.SQL_PROD_ID_QUERY, (prod_name,))
        prod_id = list_builder(cursor, 1)

        # Getting the user id in MySQL Users table
        cursor.execute(Dt.SQL_USER_ID_QUERY, (username,))
        user_id = list_builder(cursor, 1)

        # Insert ids in Saved_datas table
        cursor.execute(
            Dt.SQL_SAVE_QUERY, (
                int(user_id[0][0]),
                int(prod_id[0][0])
            )
        )
        connection.commit()

    else:
        pass
