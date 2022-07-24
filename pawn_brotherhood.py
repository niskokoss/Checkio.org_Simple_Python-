# Пешка защищена, если её клетка находится по ударом другой своей пешки.
# На игровом поле находятся только белые пешки.
# Вы должны разработать код, позволяющий определить сколько пешек защищены в этой позиции.
def safe_pawns(pawns: set) -> int:    
    x = 0
    y = {(ord(i[0]), int(i[1])) for i in pawns}
    for i in y:
        if (i[0] + 1, i[1] - 1) in y or (i[0] - 1, i[1] - 1) in y:
            x += 1
    return x


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    safe_pawns({"a8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"})
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print(safe_pawns({"a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4"}))
