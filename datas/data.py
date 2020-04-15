#########
# COMMONS
#########

# STR VAR
#########

# OpenFoodFacts licence TXT
LICENCE_TXT = "Source : OpenFoodFacts.org"
# Back to main menu TXT
BACK_TO_MAIN_TXT = "Appuyez sur Entrée pour retourner au menu principal "
# What do you (user) wan't to do ? TXT
MAIN_REQ_TXT = "Que voulez vous faire ?"

###################
# CODE.PY VARIABLES
###################

# SQL LOGS
##########

DB_HOST = "localhost"
DB_DATABASE = "P5"
DB_USER = "testeur"
DB_PASSWORD = "openclassrooms"
DB_CHARSET = "utf8mb4"

# STR VAR
#########

# Enter a username TXT
USERNAME_REQ_TXT = "Entrez un nom d'utilisateur (facultatif) : "
# Default username TXT (if user enter "")
DEFAULT_USERNAME = "all"
# Make a choice TXT
INIT_INPUT_TXT = "Faites votre choix : "

# LISTS
#######

# User's first choice list
INIT_CHOICE = [
    "1 - Trouver un substitut à un produit",
    "2 - Retrouver mes aliments substitués",
    "3 - Quitter l'application",
]

############################
# SECOND_CHOICE.PY VARIABLES
############################

# STR VAR
#########

# No subsitute saved for user TXT
NO_USER_SUB_TXT = "Aucun substitut sauvegardé pour cet utilisateur"
# Here is saved substitutes TXT
SAVED_SUB_TXT = "Voici vos substituts sauvegardés : "

# LISTS
#######

# Columns name for saved substitutes array
ARRAY_COLUMNS = ["Nom", "Magasin", "Url", "Description"]
ARRAY_LINES = ["1", "2", "3"]

###########################
# FIRST_CHOICE.PY VARIABLES
###########################

# SQL QUERY
###########

# Select all categories
SQL_CAT_QUERY = "SELECT cat_name FROM Categories ORDER BY cat_id;"

# STR VAR
#########

# Select a category TXT
CAT_INPUT_TXT = "Choisissez votre catégorie : "
# Here is the category list TXT
CAT_LIST_TXT = "Voici la liste des catégories :"
# Select a product TXT
PROD_INPUT_TXT = "Choisissez un produit : "
# Here is the product list TXT
PROD_LIST_TXT = "Voici la liste des produits : "
# User choice TXT
USER_CHOICE_TXT = "Vous avez choisis "
# Typical product url on openfoodfacts.org
PROD_URL = "https://fr.openfoodfacts.org/api/v0/product/"
# Typical category url on openfoodfacts.org
CAT_URL = "https://fr.openfoodfacts.org/category/"
# Choose a substitute to save TXT
SUB_SAVE_TXT = "Choisissez un substitut à sauvegarder : "

# LISTS
#######

# Choice list (save sub or back to main)
CHOICE_LIST = [
    "1 - Sauvegarder un des substituts",
    "2 - Retourner au menu principal",
]

######################
# HELPERS.PY VARIABLES
######################

# STR VAR
#########

# Input is not number TXT
NOT_NB_TXT = "Ce n'est pas un chiffre !"
# Input is not in index list TXT
NOT_INDEX_TXT = "Cet index n'existe pas"

########################
# API_CLASS.PY VARIABLES
########################

# API TAGS
##########

API_PROD = "product"
API_PROD_NAME = "product_name_fr"
API_NUTRI = "nutriments"
API_SUGARS = "sugars_100g"
API_FAT = "fat_100g"
API_SALT = "salt_100g"
API_CODE = "code"
API_STORES = "stores"
API_PROD_URL = "https://fr.openfoodfacts.org/produit/"
API_DESC = "generic_name_fr"

# Empty store field txt
NO_STORE_TXT = "Non renseigné"

########################
# SQL_CLASS.PY VARIABLES
########################

# SQL LOGS
##########

DB_ROOT = "root"

# SQL QUERY
###########

# Select products that belongs to chosen category
SQL_PROD_QUERY = (
    "SELECT Products.prod_name FROM Products "
    "INNER JOIN Categories "
    "ON Products.prod_cat_id = Categories.cat_id "
    "WHERE Categories.cat_name = %s "
    "ORDER BY Products.prod_score DESC "
    "LIMIT 5;"
)

# Select products score and id with its name
SQL_PROD_SC_QUERY = (
    "SELECT prod_score, prod_cat_id FROM Products " " WHERE prod_name = %s;"
)

# Select substitutes
SQL_SUB_QUERY = (
    "SELECT prod_name, prod_store, prod_url, prod_desc FROM Products "
    "WHERE prod_score < %s "
    "AND prod_cat_id = %s "
    "ORDER BY Products.prod_score "
    "LIMIT 3;"
)

# Insert a user in Users table
SQL_USER_QUERY = "INSERT IGNORE INTO Users " "(user_name) " "VALUES (%s);"

# Select user id with user name
SQL_USER_ID_QUERY = "SELECT user_id FROM Users " "WHERE user_name = %s;"

# Select prod id with prod name
SQL_PROD_ID_QUERY = "SELECT prod_id FROM Products " "WHERE prod_name = %s;"

# Insert prod id and user id in Saved_datas table
SQL_SAVE_QUERY = (
    "INSERT IGNORE INTO Saved_datas "
    "(saved_data_user_id, saved_data_prod_id) "
    "VALUES (%s, %s); "
)

# Select saved substitutes and their datas
SQL_CALL_QUERY = (
    "SELECT DISTINCT prod_name, prod_store, prod_url, prod_desc "
    "FROM Products "
    "INNER JOIN Saved_datas "
    "ON Saved_datas.saved_data_prod_id = Products.prod_id "
    "INNER JOIN Users ON Users.user_id = Saved_datas.saved_data_user_id "
    "WHERE Users.user_name = %s ;"
)

# Select all categories
SQL_CREATION_QUERY = "SELECT * FROM Categories ORDER BY cat_id;"

# Insert products and their datas in Products table
SQL_INSERT_QUERY = (
    "INSERT IGNORE INTO Products "
    "(prod_cat_id, prod_name, prod_store, "
    "prod_url, prod_score, prod_desc) "
    "VALUES (%s, %s, %s, %s, %s, %s);"
)

# STR VAR
#########

# Accent characters list
LIST_ACCENT = [
    " ",
    "À",
    "Á",
    "Â",
    "Ã",
    "Ä",
    "Å",
    "Æ",
    "Ç",
    "È",
    "É",
    "Ê",
    "Ë",
    "Ì",
    "Í",
    "Î",
    "Ï",
    "Ð",
    "Ñ",
    "Ò",
    "Ó",
    "Ô",
    "Õ",
    "Ö",
    "Ø",
    "Ù",
    "Ú",
    "Û",
    "Ü",
    "Ý",
    "Þ",
    "ß",
    "à",
    "á",
    "â",
    "ã",
    "ä",
    "å",
    "æ",
    "ç",
    "è",
    "é",
    "ê",
    "ë",
    "ì",
    "í",
    "î",
    "ï",
    "ð",
    "ñ",
    "ò",
    "ó",
    "ô",
    "õ",
    "ö",
    "ø",
    "ù",
    "ú",
    "û",
    "ü",
    "ý",
    "ý",
    "þ",
    "ÿ",
]
# Equivalent without accent
LIST_NO_ACC = [
    "-",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "C",
    "E",
    "E",
    "E",
    "E",
    "I",
    "I",
    "I",
    "I",
    "D",
    "N",
    "O",
    "O",
    "O",
    "O",
    "O",
    "O",
    "U",
    "U",
    "U",
    "U",
    "Y",
    "b",
    "s",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "c",
    "e",
    "e",
    "e",
    "e",
    "i",
    "i",
    "i",
    "i",
    "d",
    "n",
    "o",
    "o",
    "o",
    "o",
    "o",
    "o",
    "u",
    "u",
    "u",
    "u",
    "y",
    "y",
    "b",
    "y",
]

API_ID = "_id"
API_PRODUCTS = "products"

# Database doesn't exist TXT
NO_DB_TXT = "Il semble que la base de donnée n'ait pas été créée"
# SQL root password request TXT
PASSWORD_REQ_TXT = "Saisissez le mot de passe de votre root : "

# Category JSON page number min
CAT_PAGE_MIN = 1
# Category JSON page number max
CAT_PAGE_MAX = 5

# SQL script path
SCRIPT_SQL_PATH = "sql/sqlP5.sql"
