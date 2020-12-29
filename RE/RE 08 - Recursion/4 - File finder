# Created on October, 2020
# @author: Fábio Araújo de Sá

def file_finder(dirs, file_name):
    
    if dirs == file_name:
        # Se encontrar logo o pretendido:
            return file_name
         
    for i in dirs[1:]:
        # entra no segundo pedaço:
        if file_finder(i, file_name) != None:
            # Se houver algum documento dentro:
            a = dirs[0]
            b = file_finder(i, file_name)
            return f"{a}/{b}"
            # String que determina o diretório com barras
