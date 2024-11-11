# Custom python functions
def double_number(a):
    """
    Doubles the input number.

    Parameters:
    a (int or float): The number to be doubled.

    Returns:
    int or float: The doubled value of the input number.
    """
    print(f"value before double_number(): {a}")
    result = 2*a
    print(f"value after double_number(): {result}")
    return


def square_number(a):
    """
    Squares the input number.

    Parameters:
    a (int or float): The number to be squared.

    Returns:
    int or float: The squared value of the input number.
    """
    print(f"value before square_number(): {a}")
    result = a*a
    print(f"value after square_number(): {result}")
    return
