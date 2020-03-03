import requests
import json
import mysql.connector
from mysql.connector import Error
from data import *
from code_class import *

cat_list = []
prod_list = []
choice_input = ""
cat_input = ""
prod_input = ""

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
    for (id, categorie) in cursor:
        print(str(id) + " : " + categorie)
        cat_list.append(categorie)

    # User chose a category
    while input_checker(cat_input, cat_list) == False :
        cat_input = input(cat_input_txt)
        
    # Second Request - We want to display the products
    prod_query = (
        'SELECT Aliments.aliment FROM Aliments '
        'INNER JOIN Categories '
        'ON Aliments.aliment_id = Categories.id '
        'WHERE Categories.id =' 
        + cat_input + ';'
        )
    cursor.execute(prod_query)

    # Displays the ingredient list
    for row in cursor.fetchall():
       prod_list.append(row[0])

    for elem in prod_list:
        print(str(prod_list.index(elem) + 1) + " : " + elem)

    # User choose an ingredient
    while input_checker(prod_input, prod_list) == False :
        prod_input = input(prod_input_txt)

    print("Vous avez choisis " + str(prod_list[int(prod_input) - 1]))


    prod_request = requests.get("https://fr.openfoodfacts.org/category/" + str(prod_list[int(prod_input) - 1]) + ".json")
    prod_data = prod_request.json()
    
    prod_string = "Petits pois, jeunes carottes et oignons"
    user_prod = Food_name(prod_data, prod_string)
    print(user_prod.name)
    print(user_prod.brand)
    print(user_prod.url)
    print(user_prod.score)

    for dictionary in prod_data["products"] :
        if dictionary["product_name_fr"] != prod_string :
            check_string = (dictionary["product_name_fr"])
            check_prod = Food_name(prod_data, check_string)
            print(check_prod.name)     
            try :
                if float(check_prod.score) < float(user_prod.score) :
                    print("Cet aliment est plus sain")
                else :
                    print("Cet aliment n'est pas sain")
            except :
                print("pas de score sur cet aliment")
                pass


else :
    print("Le choix numéro 2 !")