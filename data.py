# User's first choice list
init_choice = [
    "1 - Trouver un substitut à un produit",
     "2 - Retrouver mes aliments substitués",
     "3 - Quitter l'application"
     ]

# User's final choice list in case "find a substitut"
end_1_choice = [
    "1 - Trouver un autre substitut à cet aliment",
    "2 - Sauvegarder cet aliment",
    "3 - Retourner au menu principal"
    ]

# Tell the user he got to make a choice
init_input_txt = "Faites votre choix : "
cat_input_txt = "Choisissez votre catégorie : "
prod_input_txt = "Choisissez un aliment : "

# Database login
dtb_user = "testeur"
# Database password
dtb_password = "openclassrooms"

# Typical product url on openfoodfacts.org
prod_url = "https://fr.openfoodfacts.org/api/v0/product/"

# Typical category url on openfoodfacts.org
cat_url = "https://fr.openfoodfacts.org/category/"

array_columns = ["Nom", "Magasin", "Url", "Substitut de"]