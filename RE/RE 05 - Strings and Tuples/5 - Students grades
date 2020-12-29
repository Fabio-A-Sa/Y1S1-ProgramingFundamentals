# Created on October, 2020
# @author: Fábio Araújo de Sá

def sort_rule(data):
    avg_grade = 100 - (float(sum(data[2]))) / (len(data[2]))
    return (avg_grade, data[0], data[1])


def sort_grades(records):
    return(tuple(sorted(records, key=sort_rule)))
