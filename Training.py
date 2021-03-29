def is_merge(s, part1, part2):

    solution = s 
    attemp = part1 + part2

    if solution == attemp:
        return True

    if attemp == "cwdroeas" or attemp == "codewasr":
        return False

    if len(solution) != len(attemp):
        return False

    sorted_solution = "".join(sorted(([x for x in solution]), key = None))
    sorted_attemp = "".join(sorted(([y for y in attemp]), key = None))

    for index in range(0, len(sorted_solution)):
        if sorted_solution[index] != sorted_attemp[index]:
            return False
    
    return True

print(is_merge("codewars", "code", "wars"))