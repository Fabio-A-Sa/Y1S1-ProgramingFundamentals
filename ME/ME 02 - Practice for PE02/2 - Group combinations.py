# Created on November, 2020
# @author: Fábio Araújo de Sá

def groups(students):

    result = ()
    
    for i in range(0, len(students)):
        for j in range(i+1, len(students)):
            for k in range(j+1, len(students)):
                
                result = result + ((students[i], students[j], students[k]), )
    
    return result


# students = ('Ana', 'Bernardo', 'Carla', 'Daniel')
# print(groups(students))
