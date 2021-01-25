
def Tabulation(n, w, cache):

    matrix = []
    W = w

    for row in range(n + 1):
        matrix.append([])
        for column in range (w + 1):
            matrix[row].append("")

    for i in range(n + 1):
        matrix[i][0] = 0

    for i in range(w + 1):
        matrix[0][i] = 0

    # ------------------------------------------

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if cache[i - 1][2] <= W:
                if cache[i - 1][1] + matrix[i - 1][W - w] > matrix[i - 1][w]:
                    matrix[i][j] = cache[i - 1][1] + matrix[i - 1][W - w]
                else:
                    matrix[i][j] = matrix[i - 1][w]
            else:
                matrix[i][w] = matrix[i - 1][w]

    for row in range(len(matrix)):
        print("\n")
        for column in range(len(matrix[row])):
            print(matrix[column])
