import mysql.connector
from mysql.connector import Error
from data import *
from code_class import *
from sql_class import *

cat_list = []
ing_list = []
choice_input = ""
cat_input = ""
ing_input = ""

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
        
    # Second Request - We want to displays ingredients
    ing_query = (
        'SELECT Aliments.aliment FROM Aliments '
        'INNER JOIN Categories '
        'ON Aliments.aliment_id = Categories.id '
        'WHERE Categories.id =' 
        + cat_input + ';'
        )
    cursor.execute(ing_query)

    # Displays the ingredient list
    for row in cursor.fetchall():
       ing_list.append(row[0])
    for elem in ing_list:
        print(str(ing_list.index(elem) + 1) + " : " + elem)

    # User choose an ingredient
    while input_checker(ing_input, ing_list) == False :
        ing_input = input(ing_input_txt)

    print("Vous avez choisis " + str(ing_list[int(ing_input) - 1]))

    cursor.close()

else :
    print("Le choix numéro 2 !")