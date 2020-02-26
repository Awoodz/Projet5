from data import *

for elem in init_choice :
    print(elem)

checker = 0

while True :
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

# Will be removed
if init_input == 1 :
    print("La liste des choix apparait !")
elif init_input == 2 :
    print("On récupère les anciennes infos")


