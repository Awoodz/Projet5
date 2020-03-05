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
            + cat_input + ';'
        )
        return query

    def save_query(name, store, url, sub_to, cursor, connection):
        """This function insert results into saved_data table"""
        # If store field is empty
        if store == "" :
            # Tell the user there was no datas
            store = "Non renseigné"
        # Insert query
        query = ("INSERT IGNORE INTO saved_data "
            "(saved_name, saved_store, saved_url, sub_to) "
            "VALUES (%s, %s, %s, %s);")
        # This format avoid tuples conflict
        cursor.execute(query, (name, store, url, sub_to,))
        # Without this, nothing is pushed in table
        connection.commit()