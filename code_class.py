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

class Food_name():

    def __init__(self, ing_data, ing_string):
        for dictionary in ing_data["products"] :
            if dictionary["product_name_fr"] == ing_string :
                try :
                    self.name = ing_string
                    self.brand = dictionary["brands"]
                    self.url = dictionary["url"]
                    self.score = dictionary["nutriments"]["nutrition-score-fr"]
                except AttributeError :
                    pass
                except KeyError :
                    pass