import requests
import json
import mysql.connector
from mysql.connector import Error
from data import *
from code_class import *

cat_list = []
prod_list = []
prod_id_list = []
choice_input = ""
cat_input = ""
prod_input = ""
sub_found = False

# Connexion to MySQL Server
connection = mysql.connector.connect (
    host = 'localhost',
    database = 'testP5',
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
    for (id, category) in cursor:
        print(str(id) + " : " + category)
        cat_list.append(category)

    # User chose a category
    while input_checker(cat_input, cat_list) == False :
        cat_input = input(cat_input_txt)
        
    # Second Request - We want to display the products
    prod_query = (
        'SELECT Products.product FROM Products '
        'INNER JOIN Categories '
        'ON Products.category_id = Categories.id '
        'WHERE Categories.id =' 
        + cat_input + ';'
        )
    cursor.execute(prod_query)

    # Displays the ingredient list
    for row in cursor.fetchall():
       prod_list.append(row[0])

    prod_query = (
        'SELECT Products.product_id FROM Products '
        'INNER JOIN Categories '
        'ON Products.category_id = Categories.id '
        'WHERE Categories.id =' 
        + cat_input + ';'
        )
    
    cursor.execute(prod_query)

    for row in cursor.fetchall():
       prod_id_list.append(row[0])
    
    for elem in prod_list:
        print(str(prod_list.index(elem) + 1) + " : " + elem)

    # User choose an ingredient
    while input_checker(prod_input, prod_list) == False :
        prod_input = input(prod_input_txt)

    print("Vous avez choisis " + str(prod_list[int(prod_input) - 1]))

    prod_request = requests.get("https://fr.openfoodfacts.org/category/" + str(cat_list[int(cat_input) - 1]).replace(" ", "-") + ".json")
    prod_data = prod_request.json()
    
    prod_string = str(prod_id_list[int(prod_input) - 1])

    user_prod = Food_name(prod_data, prod_string)
    print(user_prod.name)
    print(user_prod.brand)
    print(user_prod.url)
    print(user_prod.score)

    for dictionary in prod_data["products"] :
        if dictionary["_id"] != prod_string :
            check_string = (dictionary["_id"])
            check_prod = Food_name(prod_data, check_string)
            if sub_found == False :
                try :
                    if check_prod.score < user_prod.score :
                        substitut = Food_name(prod_data, check_string)
                        sub_found = True
                except :
                    pass
            else :
                try :
                    if check_prod.score < substitut.score :
                        substitut = Food_name(prod_data, check_string)
                except :
                    pass

    print(substitut.name)
    print(substitut.brand)
    print(substitut.url)
    print(substitut.score)
            

            
