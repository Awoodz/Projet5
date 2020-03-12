import mysql.connector
import pandas
import os

import sys
sys.path.insert(1, '/..')

from DATAS.data import *
from DATAS.helpers import *
from API.api_class import *
from SQL.sql_class import *

def first_choice(username, cursor, connection):
    """This function contains what is happening if user choose first choice"""

    cat_list = []
    prod_list = []
    prod_id_list = []
    prod_true_cat = []
    dictionary_list = []
    cat_input = ""
    prod_input = ""
    end_search = False

    # Searching categories in database
    cat_query = ('SELECT DISTINCT category FROM Categories')
    cursor.execute(cat_query)

    # Appending lists with datas from database
    for row in cursor.fetchall():
        cat_list.append(row[0])

    # Displaying the category list
    os.system('cls')
    print("Voici la liste des catégories :")
    for elem in cat_list :
        print(str(cat_list.index(elem) + 1) + " : " + elem)

    # User pick a category
    while input_checker(cat_input, cat_list) == False :
        cat_input = input(cat_input_txt)
        
    # Searching products affiliated to categories in database
    cursor.execute(Sql.prod_query(cat_input))

    # Appending lists with datas from database
    for row in cursor.fetchall():
        prod_list.append(row[0])
        prod_id_list.append(row[1])
        prod_true_cat.append(row[2])
    
    # Displaying the product list
    os.system('cls')
    print("Voici la liste des produits : ")
    for elem in prod_list:
        print(str(prod_list.index(elem) + 1) + " : " + elem)

    # User pick a product
    while input_checker(prod_input, prod_list) == False :
        prod_input = input(prod_input_txt)

    # Remind the user what he picked
    os.system('cls')
    picked_prod = str(prod_list[int(prod_input) - 1])
    print("Vous avez choisis " + picked_prod)

    # API Request about picked products
    user_data = Api.request(prod_url, list = prod_id_list, input = prod_input)

    # CLASS
    user_prod = Api(user_data)

    # API Request about products from same category than picked one    
    cat_data = Api.request(cat_url, list = prod_true_cat, input = prod_input)

    # Put all products ids from the category in a list
    for dictionary in cat_data["products"] :
        dictionary_list.append(dictionary["_id"])

    # Start the loop, as long as user wants to check others substitutes for the product he picked
    while end_search != True :

        # Searching the healthier substitude, put it in a class
        sub = Api.sub_seek(dictionary_list, user_prod)

        # Displaying informations about the substitute
        Api.answer(sub, user_prod)

        # If picked product has no substitute (it is the best), end the loop
        if sub == user_prod :
            break
        
        # Displaying possible user's actions (re-search, save, quit)
        for elem in end_1_choice :
            print(elem)

        # avoid an endless loop if user wants to re-search
        end_1_input = ""

        # user makes a choice
        while input_checker(end_1_input, end_1_choice) == False :
            end_1_input = input(init_input_txt)

        # if user wants to re-search, restart the loop
        if end_1_input == "1" :
            del dictionary_list[dictionary_list.index(sub.code)]
            sub = user_prod
            os.system('cls')
            continue
        # elif user wants to save, save the substitute datas in database, then quits
        elif end_1_input == "2" :
            try :
                Sql.save_query(cat_input, sub.name, sub.store, sub.url, picked_prod, sub.code, prod_true_cat[int(prod_input) - 1], cursor, connection, username)
            except :
                pass
            os.system('cls')
            end_search = True
        # else quits the program
        else :
            end_search = True