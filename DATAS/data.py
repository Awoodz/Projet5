###################
##### COMMONS #####
###################

##### STR VAR #####

license_txt = "Source : OpenFoodFacts.org"
back_to_main_txt = "Appuyez sur Entrée pour retourner au menu principal "

#############################
##### CODE.PY VARIABLES #####
#############################

######### SQL LOGS ##########

db_host = "localhost"
db_database = "P5"
db_user = "testeur"
db_password = "openclassrooms"
db_charset = "utf8mb4"

########## STR VAR ##########

# Enter a username TXT
username_req_txt = "Entrez un nom d'utilisateur (facultatif) : "
# Default username TXT (if user enter "")
default_username = "all"
# What do you (user) wan't to do ? TXT
main_req_txt = "Que voulez vous faire ?"
# Make a choice TXT
init_input_txt = "Faites votre choix : "

########### LISTS ###########

# User's first choice list
init_choice = [
    "1 - Trouver un substitut à un produit",
    "2 - Retrouver mes aliments substitués",
    "3 - Quitter l'application"
    ]

######################################
##### SECOND_CHOICE.PY VARIABLES #####
######################################

############## STR VAR ###############

# No subsitute saved for user TXT
no_user_sub_txt = "Aucun substitut sauvegardé pour cet utilisateur"
# Here is saved substitutes TXT
saved_sub_txt = "Voici vos substituts sauvegardés : "

############## LISTS #################

# Columns name for saved substitutes array
array_columns = ["Nom", "Magasin", "Url", "Substitut de"]

#####################################
##### FIRST_CHOICE.PY VARIABLES #####
#####################################

############# SQL QUERY #############

# Select all categories
sql_cat_query = "SELECT DISTINCT nameCAT FROM Category"

############## STR VAR ##############

# Select a category TXT
cat_input_txt = "Choisissez votre catégorie : "
# Here is the category list TXT
cat_list_txt = "Voici la liste des catégories :"
# Select a product TXT
prod_input_txt = "Choisissez un produit : "
# Here is the product list TXT
prod_list_txt = "Voici la liste des produits : "
# User choice TXT
user_choice_txt = "Vous avez choisis "
# Typical product url on openfoodfacts.org
prod_url = "https://fr.openfoodfacts.org/api/v0/product/"
# Typical category url on openfoodfacts.org
cat_url = "https://fr.openfoodfacts.org/category/"

############### LISTS ###############

# User's final choice list in case "find a substitut"
end_1_choice = [
    "1 - Trouver un autre substitut à cet aliment",
    "2 - Sauvegarder cet aliment",
    "3 - Retourner au menu principal"
    ]

################################
##### HELPERS.PY VARIABLES #####
################################

############ STR VAR ###########

# Input is not number TXT
not_nb_txt = "Ce n'est pas un chiffre !"
# Input is not in index list TXT
not_index_txt = "Cet index n'existe pas"

##################################
##### API_CLASS.PY VARIABLES #####
##################################

############ API TAGS ############

api_product = "product"
api_product_name = "product_name_fr"
api_nutriments = "nutriments"
api_sugars = "sugars_100g"
api_fat = "fat_100g"
api_salt = "salt_100g"
api_code = "code"
api_stores = "stores"
api_prod_url = "https://fr.openfoodfacts.org/produit/"

############ STR VAR ############

# Selected product is already the best TXT
healthiest_prod_txt = "Le produit sélectionné est déjà le plus sain !"
# Found subsitute is : TXT
found_sub_txt = "Le substitut trouvé est : "
# Substitute can be found at : TXT
found_store_txt = "Trouvable chez "
# No store name in API datas TXT
no_store_txt = "Malheureusement, aucun magasin n'a été renseigné"

##################################
##### SQL_CLASS.PY VARIABLES #####
##################################

############ SQL LOGS ############

db_root = "root"

############ SQL QUERY ###########

# Select products that belongs to chosen category
sql_prod_query1 = (
    "SELECT prod_name, prod_nb, true_cat FROM Products "
    "INNER JOIN Categories "
    "ON Products.cat_id = Categories.id_cat "
    "WHERE Categories.id_cat = "
)
sql_prod_query2 = " AND is_sub = 0;"

# Add the username in Users table
sql_query_11 = "INSERT IGNORE INTO Users (user_name) VALUES ('"
sql_query_12 = "');"

# Insert all the substitute datas in the Products table
sql_query_2 = (
    "INSERT IGNORE INTO Products "
    "(cat_id, prod_name, prod_stores, prod_url, sub_to, prod_nb, is_sub, true_cat) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
)

# Insert the Products id and Users id in the Subs table
sql_query_31 = (
    "INSERT IGNORE INTO Subs (prod_id, user_id) "
    "SELECT Products.id_prod, Users.id_user "
    "FROM Products, Users "
    "WHERE "
    "Products.prod_name = '"
)
sql_query_32 = (
    "' "
    "AND "
    "Users.user_name = '"
)
sql_query_33 = (
    "';"
)

# Select all substitutes (and datas) from a user
sql_call_query1 = (
    "SELECT DISTINCT prod_name, prod_stores, prod_url, sub_to FROM Products "
    "INNER JOIN Subs ON Subs.prod_id = Products.id_prod "
    "INNER JOIN Users ON Users.id_user = Subs.user_id "
    "WHERE Users.user_name = '"
)
sql_call_query2 = "';"

############# STR VAR ############

# No data about product name/store TXT
no_data_txt = "Non renseigné"
# Database doesn't exist TXT
no_db_txt = "Il semble que la base de donnée n'ait pas été créée"
# SQL root password request TXT
password_req_txt = "Saisissez le mot de passe de votre root : "
