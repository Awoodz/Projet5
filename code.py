import requests
import json
import mysql.connector
from data import *
from api_class import *
from sql_class import *
from helpers import input_checker

cat_list = []
prod_list = []
prod_id_list = []
prod_true_cat = []
dictionary_list = []
choice_input = ""
cat_input = ""
prod_input = ""
end_search = False

connection = mysql.connector.connect (
    host = 'localhost',
    database = 'P5',
    user = dtb_user,
    password = dtb_password
    )
if connection.is_connected():
    cursor = connection.cursor()

# display first request
for elem in init_choice :
    print(elem)

# User choose
while input_checker(choice_input, init_choice) == False :
    choice_input = input(init_input_txt)

if choice_input == "1" :
# First Request - We want to displays categories of ingredients
    cat_query = ('SELECT * FROM Categories')
    cursor.execute(cat_query)

    # Displaying the categories list
    print("Voici la liste des catégories :")
    for (id_cat, category) in cursor:
        print(str(id_cat) + " : " + category)
        cat_list.append(category)

    # User chose a category
    while input_checker(cat_input, cat_list) == False :
        cat_input = input(cat_input_txt)
        
    # Second Request - We want to display the products
    prod_query = (
        'SELECT prod_name, prod_nb, true_cat FROM Products '
        'INNER JOIN Categories '
        'ON Products.cat_id = Categories.id_cat '
        'WHERE Categories.id_cat =' 
        + cat_input + ';'
        )
    cursor.execute(prod_query)

    # Displays the ingredient list
    for row in cursor.fetchall():
        prod_list.append(row[0])
        prod_id_list.append(row[1])
        prod_true_cat.append(row[2])
    
    for elem in prod_list:
        print(str(prod_list.index(elem) + 1) + " : " + elem)

    # User choose an ingredient
    while input_checker(prod_input, prod_list) == False :
        prod_input = input(prod_input_txt)

    print("Vous avez choisis " + str(prod_list[int(prod_input) - 1]))

    user_data = Api.request(prod_url, list = prod_id_list, input = prod_input)

    user_prod = Api(user_data)
    
    substitut = user_prod
    
    cat_data = Api.request(cat_url, list = prod_true_cat, input = prod_input)

    for dictionary in cat_data["products"] :
        dictionary_list.append(dictionary["_id"])

    while end_search != True :

        substitut = Api.sub_seek(dictionary_list, user_prod)

        Api.answer(substitut)

        for elem in end_1_choice :
            print(elem)

        end_1_input = ""

        while input_checker(end_1_input, end_1_choice) == False :
            end_1_input = input(init_input_txt)

        if end_1_input == "1" :
            del dictionary_list[dictionary_list.index(substitut.code)]
            substitut = user_prod
            continue
        elif end_1_input == "2" :
            print("Enregistrement du substitut")
            end_search = True
        else :
            end_search = True

    print("Terminé !")
            

            
