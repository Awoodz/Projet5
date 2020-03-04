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