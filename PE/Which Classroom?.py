# Created on January, 2021
# @author: Fábio Araújo de Sá

def which_room(name):
    
    # A dict with all allowed exam's classrooms
    classrooms = {  
                    'B104': ("Adam Gershenson Nogueira", "Fábio Cunha Morais"),
                    'B201': ("Felipe Siqueira Espinheira", "Gustavo Miguel Soeiro Machado"),
                    'B207': ("Henrique Oliveira Silva", "José Marcelino Zacarias Júnior"),
                    'B208': ("José Maria Borges Pires do Couto e Castro", "Nuno André Gomes França"),
                    'B213': ("Nuno Francisco Moreira dos Santos", "Walter Muhanyele Massango") 
                 }

    # Name normalization
    name = name.strip()
    name_list = name.split(" ")

    # Find a correct classroom
    correct_classroom = ""
    counter = 0
    for key in classrooms.keys():

        # Initial conditions
        start = ((classrooms[key])[0]).split(" ")
        end = ((classrooms[key])[1]).split(" ")
        name_search = name_list[counter]

        # Search
        if name_search >= start[counter] and name_search <= end[counter]:
            correct_classroom = key

    # Get answers    
    answer_1 = "A tua sala é a {}".format(correct_classroom)
    block = correct_classroom[0]
    floor = correct_classroom[1]
    door = int(correct_classroom[2:])
    answer_2 = "Exame no bloco {}, piso {} e na porta {}".format(block, floor, door)
    
    return "{}{}{}{}{}".format(answer_1, "\n", "Informações adicionais:", "\n", answer_2)

    # name = str(input("Qual o teu nome? \n"))
    # print(which_room(name))
