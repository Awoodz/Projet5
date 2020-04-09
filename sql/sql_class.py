import mysql.connector
import getpass
from datas.data import Dt
from api.api_class import Api


class Sql():
    """This class contains all that concerns API queries"""

    def database_creation():
        """That function create database"""
        inserted_prod = 0
        score_error = 0
        name_error = 0
        print(Dt.no_db_txt)
        # asks for the password of mysql root user
        user_pass = getpass.getpass(Dt.password_req_txt)
        # connect to mysql as root

        connection = mysql.connector.connect(
            user=Dt.db_root,
            password=user_pass,
            host=Dt.db_host,
            charset=Dt.db_charset,
            use_unicode=True,
        )
        if connection.is_connected():
            cursor = connection.cursor()

        # Read the *.sql file
        read_file = open("sql/sqlP5.sql", 'r', encoding='utf8')
        sql_file = read_file.read()
        # Close it
        read_file.close()
        # Split the file at each ";"
        # so we got a list that contains full queries
        sql_query = sql_file.split(';')

        # for each query in the queries list
        try:
            for query in sql_query:
                # execute the query
                cursor.execute(query)
        except mysql.connector.errors.ProgrammingError as e:
            print(e)
            pass

        # Searching for categories and their id
        cursor.execute(Dt.sql_creation_query)

        cat_list = []
        cat_id_list = []
        # Appending lists with cursor's results
        for row in cursor.fetchall():
            cat_id_list.append(row[0])
            cat_list.append(row[1])

        # For each categories :
        i = 0
        while i < len(cat_id_list):

            cat_data = []
            dictionary_list = []

            # For each caracters in category name
            j = 0
            while j < len(Dt.list_accent):
                # Replace some characters with others, so we can use it in API
                new_cat_list = cat_list[i].replace(
                    Dt.list_accent[j],
                    Dt.list_no_acc[j]
                )
                j += 1

            # For each page of the category in API
            k = Dt.cat_page_min
            while k < Dt.cat_page_max:
                # Request a page from a category JSON (we will get products ID)
                cat_data = Api.request(Dt.cat_url, new_cat_list, k)

                # For each dictionary in the list
                for dictionary in cat_data[Dt.api_products]:
                    # Append a list with products ID
                    dictionary_list.append(dictionary[Dt.api_id])

                # For each product in the dictionary list
                for product in dictionary_list:
                    # Request datas from the product JSON page
                    prod_data = Api.request(Dt.prod_url, product, 0)
                    prod = Api(prod_data)
                    try:
                        # If product has name and description
                        if prod.name != "" and prod.desc != "":
                            try:
                                # Insert product datas in database
                                cursor.execute(
                                    Dt.sql_insert_query, (
                                        int(cat_id_list[i]),
                                        prod.name,
                                        prod.store,
                                        prod.url,
                                        float(prod.score),
                                        prod.desc
                                    )
                                )
                                connection.commit()

                                # Count succefully inserted products
                                inserted_prod += 1

                            except (AttributeError, TypeError) as e:
                                print(e)
                                # Count no score products
                                score_error += 1
                        else:
                            pass
                    except (AttributeError, TypeError) as e:
                        print(e)
                        # Count no name/description products
                        name_error += 1
                        pass
                k += 1
            i += 1

        # print results at the end
        print(str(score_error) + " produits sans score")
        print(str(name_error) + " produits sans nom/description")
        print(str(inserted_prod) + " produits ajoutés correctement")
