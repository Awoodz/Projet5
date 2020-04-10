import pandas

from datas import data as Dt
from functions.helpers import input_checker
from functions.helpers import list_builder


def first_choice(username, cursor, connection):
    """This function contains what is happening if user choose first choice"""

    sub_list = []
    cat_list = []
    prod_list = []
    prod_score = []
    cat_input = ""
    prod_input = ""
    sub_input = ""
    choice_input = ""

    # Searching categories in database
    cursor.execute(Dt.sql_cat_query)

    # Appending category list with datas from database
    for row in cursor.fetchall():
        cat_list.append(row[0])

    # As long as user's input is not valid :
    while not input_checker(cat_input, cat_list):
        # Display list title (category)
        print(Dt.cat_list_txt)
        # Display the category list
        for elem in cat_list:
            print(str(cat_list.index(elem) + 1) + " : " + elem)
        # Ask for an user input
        cat_input = input(Dt.cat_input_txt)

    # Searching products affiliated to categories in database
    cat_name = cat_list[int(cat_input) - 1]
    print(cat_name)
    cursor.execute(Dt.sql_prod_query, (cat_name,))

    # Appending product list with datas from database
    for row in cursor.fetchall():
        prod_list.append(row[0])

    # As long as user's input is not valid :
    while not input_checker(prod_input, prod_list):
        # Display list title (product)
        print(Dt.prod_list_txt)
        # Display the product list
        for elem in prod_list:
            print(str(prod_list.index(elem) + 1) + " : " + elem)
        # Ask for an user input
        prod_input = input(Dt.prod_input_txt)

    # Getting the chosen product's score and category
    prod_name = prod_list[int(prod_input) - 1]
    cursor.execute(Dt.sql_prod_sc_query, (prod_name,))

    # Building a list with score and category
    prod_score = list_builder(cursor, 2)
    # Searching for product from the same category with better score
    cursor.execute(Dt.sql_sub_query, (prod_score[0][0], prod_score[0][1]))

    # Building list with healthier products as substitutes
    sub_list = list_builder(cursor, 4)
    # Displaying the substitutes
    sub_array = pandas.DataFrame(
        sub_list, columns=Dt.array_columns, index=Dt.array_lines
    )

    print(sub_array)
    print(Dt.license_txt)

    # As long as user's input is not valid :
    while not input_checker(choice_input, Dt.choice_list):
        print(Dt.main_req_txt)
        for elem in Dt.choice_list:
            print(elem)
        choice_input = input(Dt.init_input_txt)

    if choice_input == "1":

        # User has to pick a substitute to save
        while not input_checker(sub_input, sub_list):
            print(sub_array)
            print(Dt.license_txt)
            sub_input = input(Dt.sub_save_txt)

        # Getting the name of the selected substitute
        prod_name = sub_list[int(sub_input) - 1][0]

        # Getting the product id in MySQL Products table
        cursor.execute(Dt.sql_prod_id_query, (prod_name,))
        prod_id = list_builder(cursor, 1)

        # Getting the user id in MySQL Users table
        cursor.execute(Dt.sql_user_id_query, (username,))
        user_id = list_builder(cursor, 1)

        # Insert ids in Saved_datas table
        cursor.execute(
            Dt.sql_save_query, (
                int(user_id[0][0]),
                int(prod_id[0][0])
            )
        )
        connection.commit()

    else:
        pass
