# Created on January, 2021
# @author: Fábio Araújo de Sá

def binary_tree(key, tree):

    if key == tree[0]:
        return tree[1]

    else:

        if key < tree[0]:
            next_function = tree[2]()
            return binary_tree(key, next_function)

        else:
            # If key > tree[0] or tree[0] == key
            next_function = tree[3]()
            return binary_tree(key, next_function)
