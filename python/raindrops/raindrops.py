def convert(number) -> str:
    """
    convert a number into a string
    :param number: integer
    :return: string
    """
    drops = ""
    if number % 3 == 0:
        drops += "Pling"
    if number % 5 == 0:
        drops += "Plang"
    if number % 7 == 0:
        drops += "Plong"
    if not drops:
        drops = str(number)
    return drops
