# Created on January, 2021
# @author: Fábio Araújo de Sá

def diff(filename1, filename2):

    all_lines = []
    mais = "+ "
    menos = "- "

    with open(filename1, "r") as f1:
        lines_1 = list([line for line in f1.readlines()])

    with open(filename2, "r") as f2:
        lines_2 = list([line for line in f2.readlines()])

    for line1 in lines_1:
        for line2 in lines_2:

            if lines_1.index(line1) == lines_2.index(line2):

                local_line = ""

                if line1 not in lines_2:
                    local_line = local_line + menos + line1
                    all_lines.append(local_line)

    for line1 in lines_1:
        for line2 in lines_2:

            if lines_1.index(line1) == lines_2.index(line2):

                local_line = ""

                if line2 not in lines_1:
                    local_line = local_line + mais + line2
                    all_lines.append(local_line)

    result = ""
    for item in all_lines:
        result = result + item
    
    return result
