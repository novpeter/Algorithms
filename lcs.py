def fill_matrix(x, y):
    L = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    for x_i, x_elem in enumerate(x):
        for y_i, y_elem in enumerate(y):
            if x_elem == y_elem:
                L[x_i][y_i] = L[x_i - 1][y_i - 1] + 1
            else:
                L[x_i][y_i] = max((L[x_i][y_i - 1], L[x_i - 1][y_i]))
    return L


# Есть две очень длинных строки. n1 - длина первой, n2 - длина второй строки.
# Надо в этих строках найти наибольшую подпоследовательность, которая идёт в
# одном порядке в обоих строках (пример - коллокол и молоко, общая - олоко).
# n1 * n2 < 1 000 000.
def lcs(x, y):
    L = fill_matrix(x, y)
    LCS = []
    x_i, y_i = len(x) - 1, len(y) - 1
    while x_i >= 0 and y_i >= 0:
        if x[x_i] == y[y_i]:
            LCS.append(x[x_i])
            x_i, y_i = x_i - 1, y_i - 1
        elif L[x_i - 1][y_i] > L[x_i][y_i - 1]:
            x_i -= 1
        else:
            y_i -= 1
    LCS.reverse()
    for x in LCS:
        print(x, end="")
    return LCS

lcs("коллокол", "моллоко")