import mysql.connector
from mysql.connector import Error

from data import *
from code_class import *

cat_list = []
ing_list = []
vartest = "1"
# display first request
for elem in init_choice :
    print(elem)

#################################################
#################################################
#################################################

# Connexion to MySQL Server
if input_checker(init_choice) == 1 :
    try :
        connection = mysql.connector.connect (
        host = 'localhost',
        database = 'testP5',
        user = 'testeur',
        password = 'openclassrooms'
    )
        
        if connection.is_connected():
            cursor = connection.cursor()

# First Request - We want to displays categories of ingredients
        cat_query = ('SELECT * FROM Categories')
        cursor.execute(cat_query)

# Displaying the list
        print("Voici la liste des catégories :")
        for (id, categorie) in cursor:
            print("{} : {}" .format(id, categorie))
            cat_list.append(categorie)
        print(cat_list)

        ing_query = (
            'SELECT Aliments.aliment FROM Aliments INNER JOIN Categories ON Aliments.aliment_id = Categories.id WHERE Categories.id =' + str(input_checker(cat_list)) + ';'
            )
        cursor.execute(ing_query)
        print("quelque chose s'est produit !")
        for (aliment) in cursor:
            ing_list.append(aliment)
            print("{} : {}" .format(ing_list.index(aliment) + 1, aliment))
            





        cursor.close()

    except Error as e:
        print("Une erreur est survenue, ", e)

    finally :
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("Fini")        

else :
    print("Le choix numéro 2 !")