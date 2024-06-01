# this file contains the code of the function show_in_proper_unit


def show_in_proper_unit(number):
    """
    Show the correct unit up to peta bytes
    :param number:
    :return:
    """
    if number > 10 ** 15:
        number = number / (10 ** 15)
        return number, "Po"

    elif number > 10 ** 12:
        number = number / (10 ** 12)
        return number, "To"

    elif number > 10 ** 9:
        number = number / (10 ** 9)
        return number, "Go"

    elif number > 10 ** 6:
        number = number / (10 ** 6)
        return number, "Mo"

    elif number > 10 ** 3:
        number = number / (10 ** 3)
        return number, "Ko"

    else:
        return number, ""


