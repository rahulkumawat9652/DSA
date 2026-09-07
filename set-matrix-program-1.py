matrix = [[1,2,3],[0,5,0],[3,6,0]]
def markinfinity(matrix, row, col):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(0, r):
        if matrix[i][col] != 0:
            matrix[i][col] = float("inf")
    for j in range(0, c):
        if matrix[row][j] != 0:
            matrix[row][j] = float("inf")
def setzeros(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(0, r):
        for j in range(0, c):
            if matrix[i][j] == 0:
                markinfinity(matrix, i, j)
    for i in range(0, r):
        for j in range(0, c):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0
setzeros(matrix)
print(matrix)