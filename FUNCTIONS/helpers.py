import sys
sys.path.insert(1, '/..')

from DATAS.data import *


def input_checker(user_input, choice_list):
    """ That function checks if the user entered a correct input """
    # This variable ends the "while" loop if it is True
    checker = False
    # We "try" to avoid crash if user enters a letter
    try:
        # Check if input is a int number
        user_input = int(user_input)
        # Check if input is not out of range
        if user_input < 1 or user_input > len(choice_list):
            # Warns the user input is out of range
            print(not_index_txt)
        # If input is correct, checker become True
        else:
            checker = True
    # If input is not a number
    except ValueError:
        # If user just press Enter
        if user_input == "":
            pass
        # If input was a letter, warns the user
        else:
            print(not_nb_txt)
    # Return checker, if it is True, loop ends
    return checker
