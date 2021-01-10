# Created on January, 2021
# @author: Fábio Araújo de Sá

def square_odds(values):

    if values == ("" or ","):
        return ""

    if type(values) != str:
        return ""

    if values == "0":
        return ""

    else:

        all_numbers = [int(x) for x in values.split(",")]
        all_squares = [str(x**2) for x in all_numbers if x%2==1]
        result = ",".join(all_squares)
        return result
