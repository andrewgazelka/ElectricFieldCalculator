def sqrt(number: float, iterations=100):
    """
    A binary search method for finding the square root of a number

    :param number: The number to take the square root of
    :param iterations: The number of max iterations for the square root calculation
    :return: The square root of number
    """
    if number < 1:
        on = 1  # This is so that we can still find root of small numbers like 0.00001
    else:
        on = number / 2

    dx = on / 2

    for i in range(iterations):

        if on * on > number:
            on -= dx
        elif on * on < number:
            on += dx
        else:
            return on
        dx /= 2
    return on
