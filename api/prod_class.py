import json

import requests

from datas import data as Dt


class Product:
    """This class contains all that concerns API requests or results."""

    def __init__(self, prod_data):
        """This function gathers all required datas about products."""
        # We "try" because if one of the field doesn't exist, function crash
        try:
            # Product name
            self.name = prod_data[Dt.API_PROD][Dt.API_PROD_NAME]
            # Product sugars for 100g
            self.sugar = prod_data[Dt.API_PROD][Dt.API_NUTRI][Dt.API_SUGARS]
            # Product saturated fat for 100g
            self.fat = prod_data[Dt.API_PROD][Dt.API_NUTRI][Dt.API_FAT]
            # Product salt for 100g
            self.salt = prod_data[Dt.API_PROD][Dt.API_NUTRI][Dt.API_SALT]
            # Product code
            self.code = prod_data[Dt.API_CODE]
            # Product url on openfoodfacts.org
            self.url = Dt.API_PROD_URL + self.code
            # Stores where we can find the product
            if prod_data[Dt.API_PROD][Dt.API_STORES] == "":
                self.store = prod_data[Dt.API_PROD][Dt.API_STORES]
            else:
                self.store = Dt.NO_STORE_TXT
            # Product score - determine which one is healthier
            self.score = (self.sugar + self.fat + self.salt) / 3
            # Product description
            self.desc = prod_data[Dt.API_PROD][Dt.API_DESC]
        except (AttributeError, KeyError, TypeError) as error:
            print("Erreur sur " + str(error))
            pass

    def request(url, cat, page=0):
        """This function makes requests to the API."""
        try:
            try:
                # Different parameters can be used for
                # this request, two possibilities
                if page != 0:
                    # Category request
                    user_request = requests.get(
                        url + cat + "/" + str(page) + ".json"
                    )
                else:
                    # Product request
                    user_request = requests.get(url + cat + ".json")
            except TypeError as error:
                print("TypeError" + str(error))
                pass
            return user_request.json()
        except (UnboundLocalError, json.decoder.JSONDecodeError) as error:
            print("Erreur JSON" + str(error))
            pass
