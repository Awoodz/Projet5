#CLASS

def input_checker(choice_list, input_txt) :
    """ That function checks if the user entered a correct input """
    while True :       
        user_input = input(input_txt)
        try :
            user_input = int(user_input)
        except ValueError :
            print("Ce n'est pas un chiffre !")
            continue
        if user_input < 1 or user_input > len(choice_list) :
            print("Cet index n'existe pas")
            continue
        else :
            break
        
    return user_input