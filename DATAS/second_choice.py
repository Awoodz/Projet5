import mysql.connector
import pandas
import os

import sys
sys.path.insert(1, '/..')

from DATAS.data import *
from DATAS.helpers import *
from API.api_class import *
from SQL.sql_class import *

def second_choice(username, cursor, connection):
    """This function contains what is happening if user choose second choice"""
    saved_list = []
    row_list = []

    cursor.execute(Sql.call_query(username))

    # Appending list with datas from database
    for row in cursor.fetchall():
        row_list = []
        index = 0
        # Used while to avoid repetitions
        while index != 4 :
            row_list.append(row[index])
            index = index + 1
        saved_list.append(row_list)

    # If user never saved any substitute
    if saved_list == [] :
        os.system('cls')
        print("Aucun substitut sauvegardé pour cet utilisateur")
    # Else, displays the substitute in an array
    else :
        os.system('cls')
        print("Voici vos substituts sauvegardés : ")
        sub_array = pandas.DataFrame(saved_list, columns = array_columns)
        print(sub_array)
        print("Source : OpenFoodFacts.org")
    
    input("Appuyez sur Entrée pour retourner au menu principal")