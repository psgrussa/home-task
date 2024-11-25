matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
rows = len(matrix)
cols = len(matrix[0])

for j in range(cols):
    for i in range(rows//2):
        matrix[i][j], matrix[rows - 1 - i][j] = matrix[rows - 1 - i][j], matrix[i][j]
for i in matrix:
    print(i)
