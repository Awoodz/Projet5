import mysql.connector
import getpass

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

    def save_query(cat_id, name, store, url, sub_to, nb, true_cat, cursor, connection, username):
        """This function insert results into saved_data table"""
        # First, we add username in Users table if he doesn't exist
        query1 = (
            "INSERT IGNORE INTO Users (user_name) VALUES ('" + username + "');"
        )
        cursor.execute(query1)
        # If name field is empty
        if name == "" :
            # Tell the user there was no datas
            name = "Non renseigné"
        # If store field is empty
        if store == "" :
            # Tell the user there was no datas
            store = "Non renseigné"
        # Insert query
        query = ("INSERT IGNORE INTO Products "
            "(cat_id, prod_name, prod_stores, prod_url, sub_to, prod_nb, is_sub, true_cat) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);")
        # This format avoid tuples conflict
        cursor.execute(query, (cat_id, name, store, url, sub_to, nb, 1, true_cat))
        # Without this, nothing is pushed in table
        connection.commit()
        # Last we fill Subs table with our datas
        query3 = (
            "INSERT IGNORE INTO Subs (prod_id, user_id) "
            "SELECT Products.id_prod, Users.id_user "
            "FROM Products, Users "
            "WHERE "
            "Products.prod_name = '" + name + "' "
            "AND "
            "Users.user_name = '" + username + "';"
        )
        cursor.execute(query3)
        # Without this, nothing is pushed in table
        connection.commit()



    def call_query(username):
        """This function calls back saved substituts"""
        # We look for products that are substituts and already searched by user
        query = (
            "SELECT DISTINCT prod_name, prod_stores, prod_url, sub_to FROM Products "
            "INNER JOIN Subs ON Subs.prod_id = Products.id_prod "
            "INNER JOIN Users ON Users.id_user = Subs.user_id "
            "WHERE Users.user_name = '" + username + "';"
            )
        return query

    def database_creation():
        """That function create database"""
        print("Il semble que la base de donnée n'ait pas été créée")
        # asks for the password of mysql root user
        user_pass = getpass.getpass("Saisissez le mot de passe de votre root : ")
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
        read_file = open("SQL/sqlP5.sql", 'r', encoding = 'utf8')
        sql_file = read_file.read()
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
