class Dt():

    #########
    # COMMONS
    #########

    # STR VAR
    #########

    # OpenFoodFacts licence TXT
    license_txt = "Source : OpenFoodFacts.org"
    # Back to main menu TXT
    back_to_main_txt = "Appuyez sur Entrée pour retourner au menu principal "
    # What do you (user) wan't to do ? TXT
    main_req_txt = "Que voulez vous faire ?"

    ###################
    # CODE.PY VARIABLES
    ###################

    # SQL LOGS
    ##########

    db_host = "localhost"
    db_database = "P5"
    db_user = "testeur"
    db_password = "openclassrooms"
    db_charset = "utf8mb4"

    # STR VAR
    #########

    # Enter a username TXT
    username_req_txt = "Entrez un nom d'utilisateur (facultatif) : "
    # Default username TXT (if user enter "")
    default_username = "all"
    # Make a choice TXT
    init_input_txt = "Faites votre choix : "

    # LISTS
    #######

    # User's first choice list
    init_choice = [
        "1 - Trouver un substitut à un produit",
        "2 - Retrouver mes aliments substitués",
        "3 - Quitter l'application"
        ]

    ############################
    # SECOND_CHOICE.PY VARIABLES
    ############################

    # STR VAR
    #########

    # No subsitute saved for user TXT
    no_user_sub_txt = "Aucun substitut sauvegardé pour cet utilisateur"
    # Here is saved substitutes TXT
    saved_sub_txt = "Voici vos substituts sauvegardés : "

    # LISTS
    #######

    # Columns name for saved substitutes array
    array_columns = ["Nom", "Magasin", "Url", "Description"]
    array_lines = ["1", "2", "3"]

    ###########################
    # FIRST_CHOICE.PY VARIABLES
    ###########################

    # SQL QUERY
    ###########

    # Select all categories
    sql_cat_query = "SELECT DISTINCT cat_name FROM Categories ORDER BY cat_id;"

    # STR VAR
    #########

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
    # Choose a substitute to save TXT
    sub_save_txt = "Choisissez un substitut à sauvegarder : "

    # LISTS
    #######

    # Choice list (save sub or back to main)
    choice_list = [
        "1 - Sauvegarder un des substituts",
        "2 - Retourner au menu principal",
    ]

    ######################
    # HELPERS.PY VARIABLES
    ######################

    # STR VAR
    #########

    # Input is not number TXT
    not_nb_txt = "Ce n'est pas un chiffre !"
    # Input is not in index list TXT
    not_index_txt = "Cet index n'existe pas"

    ########################
    # API_CLASS.PY VARIABLES
    ########################

    # API TAGS
    ##########

    api_prod = "product"
    api_product_name = "product_name_fr"
    api_nutri = "nutriments"
    api_sugars = "sugars_100g"
    api_fat = "fat_100g"
    api_salt = "salt_100g"
    api_code = "code"
    api_stores = "stores"
    api_prod_url = "https://fr.openfoodfacts.org/produit/"
    api_desc = "generic_name_fr"

    # Empty store field txt
    no_store_txt = "Non renseigné"

    ########################
    # SQL_CLASS.PY VARIABLES
    ########################

    # SQL LOGS
    ##########

    db_root = "root"

    # SQL QUERY
    ###########

    # Select products that belongs to chosen category
    sql_prod_query = (
        "SELECT Products.prod_name FROM Products "
        "INNER JOIN Categories "
        "ON Products.prod_cat_id = Categories.cat_id "
        "WHERE Categories.cat_name = %s "
        "ORDER BY Products.prod_score DESC "
        "LIMIT 5;"
    )

    # Select products score and id with its name
    sql_prod_sc_query = (
        "SELECT prod_score, prod_cat_id FROM Products "
        " WHERE prod_name = %s;"
    )

    # Select substitutes
    sql_sub_query = (
        "SELECT prod_name, prod_store, prod_url, prod_desc FROM Products "
        "WHERE prod_score < %s "
        "AND prod_cat_id = %s "
        "ORDER BY Products.prod_score "
        "LIMIT 3;"
    )

    # Insert a user in Users table
    sql_user_query = (
        "INSERT IGNORE INTO Users "
        "(user_name) "
        "VALUES (%s);"
    )

    # Select user id with user name
    sql_user_id_query = (
        "SELECT user_id FROM Users "
        "WHERE user_name = %s;"
    )

    # Select prod id with prod name
    sql_prod_id_query = (
        "SELECT prod_id FROM Products "
        "WHERE prod_name = %s;"
    )

    # Insert prod id and user id in Saved_datas table
    sql_save_query = (
        "INSERT IGNORE INTO Saved_datas "
        "(saved_data_user_id, saved_data_prod_id) "
        "VALUES (%s, %s); "
    )

    # Select saved substitutes and their datas
    sql_call_query = (
        "SELECT DISTINCT prod_name, prod_store, prod_url, prod_desc "
        "FROM Products "
        "INNER JOIN Saved_datas "
        "ON Saved_datas.saved_data_prod_id = Products.prod_id "
        "INNER JOIN Users ON Users.user_id = Saved_datas.saved_data_user_id "
        "WHERE Users.user_name = %s ;"
    )

    # Select all categories
    sql_creation_query = ("SELECT * FROM Categories ORDER BY cat_id;")

    # Insert products and their datas in Products table
    sql_insert_query = (
        "INSERT IGNORE INTO Products "
        "(prod_cat_id, prod_name, prod_store, "
        "prod_url, prod_score, prod_desc) "
        "VALUES (%s, %s, %s, %s, %s, %s);"
    )

    # STR VAR
    #########

    # Accent characters list
    list_accent = [
        " ", "À", "Á", "Â", "Ã", "Ä", "Å", "Æ", "Ç", "È", "É", "Ê", "Ë",
        "Ì", "Í", "Î", "Ï", "Ð", "Ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "Ø", "Ù",
        "Ú", "Û", "Ü", "Ý", "Þ", "ß", "à", "á", "â", "ã", "ä", "å", "æ",
        "ç", "è", "é", "ê", "ë", "ì", "í", "î", "ï", "ð", "ñ", "ò", "ó",
        "ô", "õ", "ö", "ø", "ù", "ú", "û", "ü", "ý", "ý", "þ", "ÿ"
    ]
    # Equivalent without accent
    list_no_acc = [
        "-", "A", "A", "A", "A", "A", "A", "A", "C", "E", "E", "E", "E",
        "I", "I", "I", "I", "D", "N", "O", "O", "O", "O", "O", "O", "U",
        "U", "U", "U", "Y", "b", "s", "a", "a", "a", "a", "a", "a", "a",
        "c", "e", "e", "e", "e", "i", "i", "i", "i", "d", "n", "o", "o",
        "o", "o", "o", "o", "u", "u", "u", "u", "y", "y", "b", "y"
    ]

    api_id = "_id"
    api_products = "products"

    # No data about product name/store TXT
    no_data_txt = "Non renseigné"
    # Database doesn't exist TXT
    no_db_txt = "Il semble que la base de donnée n'ait pas été créée"
    # SQL root password request TXT
    password_req_txt = "Saisissez le mot de passe de votre root : "

    # Category JSON page number min
    cat_page_min = 1
    # Category JSON page number max
    cat_page_max = 5

    # SQL script path
    script_sql_path = "sql/sqlP5.sql"
