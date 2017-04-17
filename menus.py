import os


def cls():
    """Clears the screen using the system, or printing 100 newlines
    Works for Macs, Windows, and *possibly* Linux, and IDE Terminals
    """
    try:
        os.system("clear")
    except:
        try:
            os.system("cls")
        except:
            print("\n" * 100)


def print_header(text, length=30):
    """Prints a message in my "Menu title" format.
    
    :param text: This is the message to print.
    :param length: This is how many characters will be in the line.
    :return: The entire text of the menu header.
    """
    cls()
    text = text.upper()
    line_len = length
    half = ((line_len - len(text))/2) - 1
    print_line = ("=" * line_len) + "\n"
    print_line += ("=" * int(half + .5) + " " + text + " " + ("=" * int(half)))
    print_line += "\n" + ("=" * line_len)
    return print_line


def print_bottom_line(length=30):
    """Prints a line out to end a menu's text.
    
    :param length: Length of the line.
    :return: the line as a string.
    """
    return "-" * length


def validate_input(user_input, valid_list):
    """Checks to see if a user's input is in a list of possible options.

    :param user_input: The input we're looking for.
    :param valid_list: The list of possible choices.
    :return: True if found, False if not (And displays error message).
    """
    try:
        if user_input[0].upper() in valid_list:
            return True
        else:
            input(invalid_choice_error(valid_list))
            return False
    except:
        input(bad_input_error())
        return False


def invalid_choice_error(valid_list):
    """Handles the error of an invalid choice in menu selection.

    :param valid_list: The list of valid choices.
    :return: string containing error message, and possible choices.
    """
    choices = ""
    for item in valid_list:
        if valid_list.index(item) <= len(valid_list) - 2:
            choices += item + ", "
        else:
            choices += "or " + item
    return "[Press Enter] Please choose a valid option: {}.".format(choices)


def bad_input_error():
    return "[Press Enter] Your input was not valid. Please try again."


def main_menu():
    while True:
        cls()
        valid_options = ["", "", "", "", "", "", ""]
        print_header("main menu")
        print_bottom_line()
        choice = input("> ")
        if validate_input(input(""), valid_options):
            pass
        else:
            pass


def search_menu():
    cls()
    valid_options = ["", "", "", "", "", "", ""]
    print_header("search menu")


def edit_menu():
    cls()
    valid_options = ["", "", "", "", "", "", ""]
    print_header("edit menu")
