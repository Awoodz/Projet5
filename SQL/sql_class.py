import mysql.connector
import getpass

import sys
sys.path.insert(1, '/..')

from DATAS.data import *
from API.api_class import Api


class Sql():
    """This class contains all that concerns API queries"""

    def database_creation():
        """That function create database"""
        inserted_prod = 0
        score_error = 0
        name_error = 0
        print(no_db_txt)
        # asks for the password of mysql root user
        user_pass = getpass.getpass(password_req_txt)
        # connect to mysql as root
        connection = mysql.connector.connect(
            user=db_root,
            password=user_pass,
            host=db_host,
            charset=db_charset,
            use_unicode=True,
        )
        if connection.is_connected():
            cursor = connection.cursor()

        # Read the *.sql file
        read_file = open("SQL/sqlP5.sql", 'r', encoding='utf8')
        sql_file = read_file.read()
        # Close it
        read_file.close()
        # Split the file at each ";"
        # so we got a list that contains full queries
        sql_query = sql_file.split(';')

        # for each query in the queries list
        for query in sql_query:
            try:
                # execute the query
                cursor.execute(query)
            except:
                pass
        cursor.execute("USE P5;")
        cursor.execute("SELECT * FROM Categories ORDER BY cat_id;")
        cat_list = []
        cat_id_list = []
        for row in cursor.fetchall():
            cat_id_list.append(row[0])
            cat_list.append(row[1])

        i = 0
        while i < len(cat_id_list):
            
            cat_data = []
            dictionary_list = []
            list_accent = [" ", "é", "â", "à"]
            list_no_acc = ["-", "e", "a", "a"]

            j = 0
            while j < len(list_accent):
                new_cat_list = cat_list[i].replace(list_accent[j], list_no_acc[j])
                j += 1
                
            k = 1
            while k < 5:
                cat_data = Api.request(cat_url, new_cat_list, k)

                for dictionary in cat_data["products"]:
                    dictionary_list.append(dictionary["_id"])

                for tags in dictionary_list :
                    prod_data = Api.request(prod_url, tags, 0)
                    prod = Api(prod_data)
                    try :
                        if prod.name != "":
                            try :
                                print(prod.desc)
                                query = (
                                    "INSERT IGNORE INTO Products "
                                    "(prod_cat_id, prod_name, prod_store, prod_url, prod_score, prod_desc) " 
                                    "VALUES (%s, %s, %s, %s, %s, %s);"
                                    )
                                cursor.execute(query, (int(cat_id_list[i]), prod.name, prod.store, prod.url, float(prod.score), prod.desc))
                                connection.commit()

                                inserted_prod += 1
                            
                            except AttributeError:
                                score_error += 1
                        else:
                            pass
                    except AttributeError:
                        name_error += 1
                        pass
                k += 1
            i += 1
        
        print(str(score_error) + " produits sans score")
        print(str(name_error) + " produits sans nom")
        print(str(inserted_prod) + " produits ajoutés correctement")
