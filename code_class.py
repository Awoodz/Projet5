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


