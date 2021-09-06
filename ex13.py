"""
Вам предоставляется набор координат, в которых расставлены белые пешки.
Вы должны подсчитать количество защищенных пешек.

Входные данные: Координаты расставленных пешек в виде набора строк.
Выходные данные: Количество защищенных пешек в виде целого числа.
"""

def safe_pawns(pawns: set) -> int:
    defenced = 0
    pawns = list(pawns)
    print(pawns)
    for pawn in pawns:
        p_l = chr(ord(pawn[0]) - 1)  # previous letter
        n_l = chr(ord(pawn[0]) + 1)  # next letter
        p_p = str(int(pawn[1]) - 1)  # previous position
        if (p_l + p_p in pawns) or (n_l + p_p in pawns):

            defenced += 1
            print(pawn)
        else:
            continue
    return defenced


print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))
#safe_pawns({"b2", "a1"})
# m = {"b1", "c2", "c3"}
# if "b" + str(1) in m:
#     print("JFD")
# u = "b1"
# for i in m:
#     print(str(chr(ord(i[0]) + 1)) + str(i[1]))
# print(chr(ord(u[0])  +1))