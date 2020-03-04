#CLASS


def input_checker(user_input, choice_list) :
    """ That function checks if the user entered a correct input """
    checker = False
    try :
        user_input = int(user_input)
        if user_input < 1 or user_input > len(choice_list) :
            print("Cet index n'existe pas")
        else :
            checker = True
    except ValueError :
        if user_input == "" :
            pass
        else :
            print("Ce n'est pas un chiffre !")
    return checker

class Product_attribute():

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

        