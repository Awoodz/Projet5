import mysql.connector

class Sql():
    """This class contains all that concerns API queries"""

    def prod_query(cat_input) :
        """This function call products table on database"""
        # Select query
        query = (
            'SELECT prod_name, prod_nb, true_cat FROM Products '
            'INNER JOIN Categories '
            'ON Products.cat_id = Categories.id_cat '
            'WHERE Categories.id_cat =' 
            + cat_input + ' AND is_sub = 0;'
        )
        return query

    def save_query(cat_id, name, store, url, sub_to, nb, true_cat, username, cursor, connection):
        """This function insert results into saved_data table"""
        # If name field is empty
        if name == "" :
            # Tell the user there was no datas
            name = "Non renseigné"
        # If store field is empty
        if store == "" :
            # Tell the user there was no datas
            store = "Non renseigné"
        # Insert query
        query = ("INSERT IGNORE INTO products "
            "(cat_id, prod_name, prod_stores, prod_url, sub_to, prod_nb, is_sub, true_cat, user) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
        # This format avoid tuples conflict
        cursor.execute(query, (cat_id, name, store, url, sub_to, nb, 1, true_cat, username))
        # Without this, nothing is pushed in table
        connection.commit()

    def call_query(username):
        """This function calls back saved substituts"""
        # We look for products that are substituts and already searched by user
        query = (
            "SELECT prod_name, prod_stores, prod_url, sub_to FROM Products WHERE user = '" + username + "';"
            )
        return query

    def database_creation():
        """That function create database"""
        print("Il semble que la base de donnée n'ait pas été créée")
        # asks for the password of mysql root user
        user_pass = input("Veuillez saisir le mot de passe de votre root : ")
        # connect to mysql as root
        connection = mysql.connector.connect(
            user = 'root',
            password = user_pass,
            host = 'localhost',
            charset = 'utf8mb4',
            use_unicode = True,
            )
        if connection.is_connected():
            cursor = connection.cursor()

        # Read the *.sql file
        read_file = open("sauvegardeP5.sql", 'r', encoding = 'utf8')
        sql_file = read_file.read()
        print(sql_file)
        # Close it
        read_file.close()
        # Split the file at each ";" so we got a list that contains full queries
        sql_query = sql_file.split(';')
        

        # for each query in the queries list
        for query in sql_query:
            try:
                # execute the query
                cursor.execute(query)
            except :
                pass
