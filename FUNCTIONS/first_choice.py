import pandas
import os
import sys
sys.path.insert(1, '/..')
from DATAS.data import *
from FUNCTIONS.helpers import input_checker
from FUNCTIONS.helpers import list_builder
from API.api_class import Api
from SQL.sql_class import Sql


def first_choice(username, cursor, connection):
    """This function contains what is happening if user choose first choice"""

    sub_list = []
    row_list = []
    cat_list = []
    prod_list = []
    prod_id_list = []
    prod_score = []
    prod_cat_id = []
    sub_name = []
    sub_store = []
    sub_url = []
    cat_input = ""
    prod_input = ""
    sub_input = ""
    
    # Searching categories in database
    cat_query = (sql_cat_query)
    cursor.execute(cat_query)

    # Appending category list with datas from database
    for row in cursor.fetchall():
        cat_list.append(row[0])

    # As long as user's input is not valid :
    while not input_checker(cat_input, cat_list):
        # Display list title (category)
        print(cat_list_txt)
        # Display the category list
        for elem in cat_list:
            print(str(cat_list.index(elem) + 1) + " : " + elem)
        # Ask for an user input
        cat_input = input(cat_input_txt)

    # Searching products affiliated to categories in database
    cursor.execute(sql_prod_query, ((cat_list[int(cat_input) - 1]),))

    # Appending product list with datas from database
    for row in cursor.fetchall():
        prod_list.append(row[0])

    # As long as user's input is not valid :
    while not input_checker(prod_input, prod_list):
        # Display list title (product)
        print(prod_list_txt)
        # Display the product list
        for elem in prod_list:
            print(str(prod_list.index(elem) + 1) + " : " + elem)
        # Ask for an user input
        prod_input = input(prod_input_txt)

    # Getting the chosen product's score and category
    cursor.execute(sql_prod_score_query, ((prod_list[int(prod_input) - 1]),))

    # Building a list with score and category
    prod_score = list_builder(cursor, 2)
    # Searching for product from the same category with better score
    cursor.execute(sql_sub_query, (prod_score[0][0], prod_score[0][1]))

    # Building list with healthier products as substitutes
    sub_list = list_builder(cursor, 4)
    # Displaying the substitutes
    sub_array = pandas.DataFrame(sub_list, columns=array_columns, index=array_lines)

    
    while not input_checker(sub_input, sub_list):
        print(sub_array)
        sub_input = input("Sélection du sub : ")
    
    prod_name = sub_list[int(sub_input) - 1][0]


    cursor.execute(sql_prod_id_query, (prod_name,))
    prod_id = list_builder(cursor, 1)

    cursor.execute(sql_user_id_query, (username,))
    user_id = list_builder(cursor, 1)

    cursor.execute(sql_save_query, (int(user_id[0][0]), int(prod_id[0][0])))
    connection.commit()

    input("Pressez entrée pour quitter")