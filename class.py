#CLASS

def input_checker(choice_list) :
""" That function checks if the user entered a correct input """
    while checker != 1 :
        init_input = input("Entrez le numéro de votre sélection : ")
        try :
            init_input = int(init_input)
        except ValueError :
            print("Ce n'est pas un chiffre !")
            continue
        if init_input < 1 or init_input > len(init_choice) :
            print("Cet index n'existe pas")
            continue
        else :
            break