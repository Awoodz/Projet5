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
        try:
            # Product name
            self.name = prod_data[api_product][api_product_name]
            # Product sugars for 100g
            self.sugar = prod_data[api_product][api_nutriments][api_sugars]
            # Product saturated fat for 100g
            self.fat = prod_data[api_product][api_nutriments][api_fat]
            # Product salt for 100g
            self.salt = prod_data[api_product][api_nutriments][api_salt]
            # Product code
            self.code = prod_data[api_code]
            # Product url on openfoodfacts.org
            self.url = (api_prod_url + self.code)
            # Stores where we can find the product
            self.store = prod_data[api_product][api_stores]
            # Product score - determine which one is healthier
            self.score = (self.sugar + self.fat + self.salt) / 3

        except AttributeError:
            pass
        except KeyError:
            pass

    def request(url, list=[], input="", other=0):
        """This function makes requests to the API"""
        # Different parameters can be used for this request, two possibilities
        if other == 0:
            user_request = requests.get(
                url + str(list[int(input) - 1]) + ".json"
            )
        # Second possibility
        else:
            user_request = requests.get(url + str(other) + ".json")
        return user_request.json()

    def sub_seek(dictionary_list, user_prod):
        """This function looks for an healthier product in the category.json"""
        # Sub is going to be reused many times outside the function
        global sub
        # Check if, at least, one subsitut was found
        sub_found = False
        # For each product id in the list
        for elem in dictionary_list:
            # Request product .json
            prod_data = Api.request(prod_url, other=elem)
            # Checked product belong to Api class, so we can read its datas
            check_prod = Api(prod_data)
            # If no substitut was found
            if sub_found == False:
                try:
                    # Compares checked product and product user selected
                    if check_prod.score < user_prod.score:
                        # If checked product is better, it become the substitut
                        sub = Api(prod_data)
                        # ...so a substitut was found !
                        sub_found = True
                except:
                    pass
            # If a substitut was found
            else:
                try:
                    # Compares checked product and subsitut
                    if check_prod.score < sub.score:
                        # If checked product is better,
                        # it become the new substitut
                        sub = Api(prod_data)
                except:
                    pass
        # If after all products where checked, no substitut was found
        if sub_found == False:
            # Means that the product user selected is already the better
            sub = user_prod
        return sub

    def answer(substitut, user_prod):
        """This function displays results to the user"""
        # Answer if product user selected is already the best
        if substitut == user_prod:
            print(healthiest_prod_txt)
            input(back_to_main_txt)
        # Answer if a subsitut was found
        else:
            # Give its name"
            print(found_sub_txt + substitut.name)
            # If stores field was not empty
            if substitut.store != "":
                # Give store's name(s) where product is
                print(found_store_txt + substitut.store)
            else:
                # Else, no luck !
                print(no_store_txt)
            # Give its url on openfoodfacts.org
            print(substitut.url)
            # Credit the API (licence specification)
            print(license_txt)
