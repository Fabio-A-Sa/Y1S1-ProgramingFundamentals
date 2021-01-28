# Created on January, 2021
# @author: Fábio Araújo de Sá

def nested_exceptions(tree):

    all_answers = []

    for item in tree:

        # Base case, is a function
        if callable(item):
            try:
                item()
                all_answers.append(False)
            except:
                all_answers.append(True)

        else:
            # Recursive search
            something = nested_exceptions(item)
            all_answers.append(something)

    answers = tuple(all_answers)
    return answers
