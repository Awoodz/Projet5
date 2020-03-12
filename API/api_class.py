import json
import requests

import sys
sys.path.insert(1, '/..')

from DATAS.data import *

class Api():
    """This class contains all that concerns API requests or results"""

    def __init__(self, prod_data):
        """This function gathers all required datas about products"""
        # We "try" because if one of the field doesn't exist, function crash
        try :
            # Product name
            self.name = prod_data["product"]["product_name_fr"]
            # Product sugars for 100g
            self.sugar = prod_data["product"]["nutriments"]["sugars_100g"]
            # Product saturated fat for 100g
            self.fat = prod_data["product"]["nutriments"]["fat_100g"]
            # Product salt for 100g
            self.salt = prod_data["product"]["nutriments"]["salt_100g"]
            # Product url on openfoodfacts.org
            self.url = ("https://fr.openfoodfacts.org/produit/" + prod_data["code"])
            # Stores where we can find the product
            self.store = prod_data["product"]["stores"]
            # Product score - determine which one is healthier
            self.score = (self.sugar + self.fat + self.salt) / 3
            # Product code
            self.code = prod_data["code"]
        except AttributeError :
            pass
        except KeyError :
            pass

    def request(url, list = [], input = "", other = 0) :
        """This function makes requests to the API"""
        # Different parameters can be used for this request, two possibilities
        if other == 0 :
            user_request = requests.get(url + str(list[int(input) - 1]) + ".json")
        # Second possibility
        else :
            user_request = requests.get(url + str(other) + ".json")
        return user_request.json()

    def sub_seek(dictionary_list, user_prod):
        """This function looks for an healthier product in the category.json"""
        # Sub is going to be reused many times outside the function
        global sub
        # Check if, at least, one subsitut was found
        sub_found = False
        # For each product id in the list
        for elem in dictionary_list :
            # Request product .json
            prod_data = Api.request(prod_url, other = elem)
            # Checked product belong to Api class, so we can read its datas
            check_prod = Api(prod_data)
            # If no substitut was found
            if sub_found == False :
                try :
                    # Compares checked product and product user selected
                    if check_prod.score < user_prod.score :
                        # If checked product is better, it become the substitut
                        sub = Api(prod_data)
                        # ...so a substitut was found !
                        sub_found = True
                except :
                    pass
            # If a substitut was found
            else :
                try :
                    # Compares checked product and subsitut
                    if check_prod.score < sub.score :
                        # If checked product is better, it become the new substitut
                        sub = Api(prod_data)
                except :
                    pass
        # If after all products where checked, no substitut was found
        if sub_found == False :
            # Means that the product user selected is already the better
            sub = user_prod
        return sub
        
    def answer(substitut, user_prod) :
        """This function displays results to the user"""
        # Answer if product user selected is already the best
        if substitut == user_prod :
            print("Le produit sélectionné est déjà le plus sain !")
        # Answer if a subsitut was found
        else :
            # Give its name"
            print("Le substitut trouvé est : " + substitut.name)
            # If stores field was not empty
            if substitut.store != "" :
                # Give store's name(s) where product is
                print("Trouvable chez " + substitut.store)
            else :
                # Else, no luck !
                print("Malheureusement, aucun magasin n'a été renseigné")
            # Give its url on openfoodfacts.org
            print(substitut.url)
            # Credit the API (licence specification)
            print("Source : OpenFoodFacts.org")