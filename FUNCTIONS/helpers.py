from datas.data import Dt


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
            print(Dt.not_index_txt)
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
            print(Dt.not_nb_txt)
    # Return checker, if it is True, loop ends
    return checker


def list_builder(cursor, i):
    """This function build list with datas from MySQL cursor"""
    ret_list = []
    # For each row in cursor
    for row in cursor.fetchall():
        # Reseting row list for each occurence
        row_list = []
        index = 0
        # As long as index != i
        while index != i:
            # Appending the row list
            row_list.append(row[index])
            index = index + 1
        # Then appending another list with row list
        ret_list.append(row_list)
    return ret_list
