matrix = [
    [1, 2, 3, 10],
    [4, 5, 6, 11],
    [7, 8, 9, 12]]

rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0
new_matrix = []
for i in range(cols):
    new_matrix.append([0] * rows)

for i in range(rows):
    for j in range(cols):
        new_matrix[j][i] = matrix[i][j]

for i in new_matrix:
    print(i)
