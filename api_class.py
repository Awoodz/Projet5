import json
import requests
from data import *

class Api():

    def __init__(self, prod_data):
        try :
            self.name = prod_data["product"]["product_name_fr"]
            self.sugar = prod_data["product"]["nutriments"]["sugars_100g"]
            self.fat = prod_data["product"]["nutriments"]["fat_100g"]
            self.salt = prod_data["product"]["nutriments"]["salt_100g"]
            self.url = ("https://fr.openfoodfacts.org/produit/" + prod_data["code"])
            self.store = prod_data["product"]["stores"]
            self.score = (self.sugar + self.fat + self.salt) / 3
            self.code = prod_data["code"]
        except AttributeError :
            pass
        except KeyError :
            pass

    def request(url, list = [], input = "", other = 0) :
        if other == 0 :
            user_request = requests.get(url + str(list[int(input) - 1]) + ".json")
        else :
            user_request = requests.get(url + str(other) + ".json")

        return user_request.json()

    def sub_seek(dictionary_list, user_prod):
        global substitut
        sub_found = False
        for elem in dictionary_list :
            prod_data = Api.request(prod_url, other = elem)
            check_prod = Api(prod_data)
            if sub_found == False :
                try :
                    if check_prod.score < user_prod.score :
                        substitut = Api(prod_data)
                        sub_found = True
                except :
                    pass
            else :
                try :
                    if check_prod.score < substitut.score :
                        substitut = Api(prod_data)
                except :
                    pass
        if sub_found == False :
            substitut = user_prod
        return substitut
        
    def answer(substitut, user_prod) :
        if substitut == user_prod :
            print("Le produit sélectionné est déjà le plus sain !")
        else :
            print("Le substitut trouvé est : " + substitut.name)
            if substitut.store != "" :
                print("Trouvable chez " + substitut.store)
            else :
                print("Malheureusement, aucun magasin n'a été renseigné")
            print(substitut.url)
            print("Source : OpenFoodFacts.org")