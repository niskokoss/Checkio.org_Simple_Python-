OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == OPERATION_NAMES[0]:
        return 1 if x and y == 1 else 0
    if operation == OPERATION_NAMES[1]:
        return 1 if x or y == 1 else 0
    if operation == OPERATION_NAMES[2]:
        return 1 if x == 0 or y == 1 else 0
    if operation == OPERATION_NAMES[3]:
        return 1 if x != y else 0
    if operation == OPERATION_NAMES[4]:
        return 1 if x == y else 0




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print('All good! Go and check the mission.')
