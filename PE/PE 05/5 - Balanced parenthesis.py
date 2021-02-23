# Created on February, 2021
# @author: Fábio Araújo de Sá

def balanced_parenthesis(expression):

    if len(expression) in [0, 1] or expression in [')(', '][']:
        return -1

    else:

        retos = ""
        curvos = ""
        total = ""

        mirror =    {
                        ")" : "(",
                        "(" : ")",
                        "[" : "]",
                        "]" : "[",
                    }

        for char in expression:
            if char == ")" or char == "(":
                curvos = curvos + char
                total = total + char
            elif char == "]" or char == "[":
                retos = retos + char
                total = total + char
            else:
                continue
        
        qdt_retos = len(retos)
        qdt_curvos = len(curvos)

        flag = (qdt_curvos % 2 == 0) and (qdt_retos % 2 == 0)
        if flag:

            for index in range(qdt_curvos // 2):
                flag = flag and (curvos[index] != curvos[-index-1])

            for index in range(qdt_retos // 2):
                flag = flag and (retos[index] != retos[-index-1])

            if flag:

                qtd_total = len(total) // 2
                for index in range(qtd_total):
                    char = total[index]
                    flag = flag and (mirror[char] == total[-index-1])

                if flag:
                    number_of_pairs = ( len(retos) + len(curvos) ) // 2
                    return number_of_pairs

                else:
                    return -1
            else:
                return -1
        else:
            return -1


# expression = "(2 + [3 * 5 / 78 + [23 / 34 - (89 * 3)])]"
# print(balanced_parenthesis(expression))