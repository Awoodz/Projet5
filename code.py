import requests
import json
import mysql.connector
from mysql.connector import Error
from data import *
from code_class import *

cat_list = []
prod_list = []
prod_id_list = []
dictionary_list = []
choice_input = ""
cat_input = ""
prod_input = ""
sub_found = False
end_search = False

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

    user_request = requests.get("https://world.openfoodfacts.org/api/v0/product/" + str(prod_id_list[int(prod_input) - 1]) + ".json")
    user_data = user_request.json()

    user_prod = Product_attribute(user_data)
    
    cat_request = requests.get("https://fr.openfoodfacts.org/category/" + str(cat_list[int(cat_input) - 1]).replace(" ", "-") + ".json")
    cat_data = cat_request.json()

    for dictionary in cat_data["products"] :
        dictionary_list.append(dictionary["_id"])

    while end_search != True :
        for elem in dictionary_list :
            prod_request = requests.get("https://world.openfoodfacts.org/api/v0/product/" + str(elem) + ".json")
            prod_data = prod_request.json()
            check_prod = Product_attribute(prod_data)
            if sub_found == False :
                try :
                    if check_prod.score < user_prod.score :
                        substitut = Product_attribute(prod_data)
                        sub_found = True
                except :
                    pass
            else :
                try :
                    if check_prod.score < substitut.score :
                        substitut = Product_attribute(prod_data)
                except :
                    pass

        print("Le substitut trouvé est : " + substitut.name)
        if substitut.store != "" :
            print("Trouvable chez " + substitut.store)
        else :
            print("Malheureusement, aucun magasin n'a été renseigné")
        print(substitut.url)
        print("Source : OpenFoodFacts.org")

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
            

            
