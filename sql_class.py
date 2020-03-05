import mysql.connector

class Sql():

    def prod_query(cat_input) :
        query = (
            'SELECT prod_name, prod_nb, true_cat FROM Products '
            'INNER JOIN Categories '
            'ON Products.cat_id = Categories.id_cat '
            'WHERE Categories.id_cat =' 
            + cat_input + ';'
        )
        return query

    def save_query(name, store, url, sub_to, cursor, connection):
        if store == "" :
            store = "Non renseigné"
        query = ("INSERT IGNORE INTO saved_data "
            "(saved_name, saved_store, saved_url, sub_to) "
            "VALUES (%s, %s, %s, %s);")
        cursor.execute(query, (name, store, url, sub_to,))
        connection.commit()