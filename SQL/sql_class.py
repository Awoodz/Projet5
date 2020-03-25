import mysql.connector
import getpass

import sys
sys.path.insert(1, '/..')

from DATAS.data import *


class Sql():
    """This class contains all that concerns API queries"""

    def prod_query(cat_input):
        """This function call products table on database"""
        # Select query
        query = (sql_prod_query1 + cat_input + sql_prod_query2)
        return query

    def save_query(
            cat_id, name, store, url,
            sub_to, nb, true_cat,
            cursor, connection, username):
        """This function insert results into saved_data table"""

        # First, we add username in Users table if he doesn't exist
        query_1 = (sql_query_11 + username + sql_query_12)
        cursor.execute(query_1)
        # If name field is empty
        if name == "":
            # Tell the user there was no datas
            name = no_data_txt
        # If store field is empty
        if store == "":
            # Tell the user there was no datas
            store = no_data_txt
        # Insert query
        query_2 = sql_query_2
        cursor.execute(query_2, (
            cat_id, name, store,
            url, sub_to, nb, 1, true_cat
        ))
        # Without this, nothing is pushed in table
        connection.commit()
        # Last we fill Subs table with our datas
        query_3 = (
            sql_query_31
            + name
            + sql_query_32
            + username
            + sql_query_33
        )
        cursor.execute(query_3)
        # Without this, nothing is pushed in table
        connection.commit()

    def call_query(username):
        """This function calls back saved substituts"""
        # We look for products that are substituts and already searched by user
        query = (
            sql_call_query1 +
            username +
            sql_call_query2
        )
        return query

    def database_creation():
        """That function create database"""
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
