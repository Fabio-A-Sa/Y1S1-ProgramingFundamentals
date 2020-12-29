# Created on November, 2020
# @author: Fábio Araújo de Sá

def iterate_rev(names, numbers, emails):
    
    result = ""
    
    for i in range(len(names)):
        result = "{} - {} - {}\n{}".format(names[i], numbers[i], emails[i], result)

    return result

# names = ("ana", "bernardo", "carlos")
# numbers = (938421028, 916381961, 939090082)
# emails=("ana.serra@gmail.com", "b1999@hotmail.com", "up201945321@fe.up.pt")
# print(iterate_rev(names, numbers, emails))
