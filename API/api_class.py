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
            # Product description
            self.desc = prod_data[api_product][api_desc]

        except AttributeError:
            pass
        except KeyError:
            pass

    def request(url, cat, page = 0):
        """This function makes requests to the API"""
        try:
            try:
                if page != 0 :
                # Different parameters can be used for this request, two possibilities
                    user_request = requests.get(url + cat + "/" + str(page) + ".json")
                else:
                    user_request = requests.get(url + cat + ".json")
            except TypeError:
                print("TypeError")
                pass
            return user_request.json()
        except UnboundLocalError:
            print("UnboundLocalError")
            pass
