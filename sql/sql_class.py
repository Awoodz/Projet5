import mysql.connector

import getpass

from datas import data as Dt
from api.prod_class import Product


class Sql:
    """This class contains database creation code."""

    def database_creation():
        """That function create database."""
        inserted_prod = 0
        score_error = 0
        name_error = 0
        print(Dt.NO_DB_TXT)
        # asks for the password of mysql root user
        user_pass = getpass.getpass(Dt.PASSWORD_REQ_TXT)
        # connect to mysql as root

        connection = mysql.connector.connect(
            user=Dt.DB_ROOT,
            password=user_pass,
            host=Dt.DB_HOST,
            charset=Dt.DB_CHARSET,
            use_unicode=True,
        )
        if connection.is_connected():
            cursor = connection.cursor()

        # Read the *.sql file
        read_file = open("sql/sqlP5.sql", "r", encoding="utf8")
        sql_file = read_file.read()
        # Close it
        read_file.close()
        # Split the file at each ";"
        # so we got a list that contains full queries
        sql_query = sql_file.split(";")

        # for each query in the queries list
        try:
            for query in sql_query:
                # execute the query
                cursor.execute(query)
        except mysql.connector.errors.ProgrammingError as error:
            print(error)
            pass

        # Searching for categories and their id
        cursor.execute(Dt.SQL_CREATION_QUERY)

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
            while j < len(Dt.LIST_ACCENT):
                # Replace some characters with others, so we can use it in API
                new_cat_list = cat_list[i].replace(
                    Dt.LIST_ACCENT[j],
                    Dt.LIST_NO_ACC[j]
                )
                j += 1

            # For each page of the category in API
            k = Dt.CAT_PAGE_MIN
            while k < Dt.CAT_PAGE_MAX:
                # Request a page from a category JSON (we will get products ID)
                cat_data = Product.request(Dt.CAT_URL, new_cat_list, k)

                # For each dictionary in the list
                for dictionary in cat_data[Dt.API_PRODUCTS]:
                    # Append a list with products ID
                    dictionary_list.append(dictionary[Dt.API_ID])

                # For each product in the dictionary list
                for product in dictionary_list:
                    # Request datas from the product JSON page
                    prod_data = Product.request(Dt.PROD_URL, product, 0)
                    prod = Product(prod_data)
                    try:
                        # If product has name and description
                        if prod.name != "" and prod.desc != "":
                            try:
                                # Insert product datas in database
                                cursor.execute(
                                    Dt.SQL_INSERT_QUERY,
                                    (
                                        int(cat_id_list[i]),
                                        prod.name,
                                        prod.store,
                                        prod.url,
                                        float(prod.score),
                                        prod.desc,
                                    ),
                                )
                                connection.commit()

                                # Count succefully inserted products
                                inserted_prod += 1

                            except (AttributeError, TypeError) as error:
                                print(error)
                                # Count no score products
                                score_error += 1
                        else:
                            pass
                    except (AttributeError, TypeError) as error:
                        print(error)
                        # Count no name/description products
                        name_error += 1
                        pass
                k += 1
            i += 1

        # print results at the end
        print(str(score_error) + " produits sans score")
        print(str(name_error) + " produits sans nom/description")
        print(str(inserted_prod) + " produits ajoutés correctement")
