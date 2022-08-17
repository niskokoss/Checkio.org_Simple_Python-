# В математике и математической логике,
# Булева алгебра это подраздел алгебры, в котором значения переменных истинны или ложны, и обычно обозначенны 0 или 1 соответственно.
# В отличии от простой алгебры, где значение переменных — это числа, и основные операции это сложение и умножение, основные операции
# Булевой алегбры это конъюнкция — ∧, дизъюнкция — ∨, и отрицание — ¬.

# В этой миссии вам нужно реализовать несколько булевых операций:
# • конъюнкция ("conjunction") обозначенная x ∧ y, удовлетворяющая условиям x ∧ y = 1 если x = y = 1 и x ∧ y = 0 иначе.
# • дизъюнкция ("disjunction") обозначенная x ∨ y, удовлетворяющая условиям x ∨ y = 0 если x = y = 0 и x ∨ y = 1 иначе.
# • импликация ("implication") (прямая импликация) обозначенная x→y и описанная как ¬ x ∨ y. Если x это истина, тогда значение x → y берётся такое, как y. Но если x — ложь, тогда результат будет истина без учёта значения y.
# • исключение ("exclusive") (исключающее ИЛИ) обозначенное x ⊕ y и описанное как (x ∨ y)∧ ¬ (x ∧ y). Результат истина если x и y различны, и ложь в противном случае. В терминах арифметики, это сложение по модулю 2, где 1 + 1 = 0.
# • эквивалентность ("equivalence") обозначенная x ≡ y и описанная как ¬ (x ⊕ y). Это истина, когда x и y имеют одинаковые значения.

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
