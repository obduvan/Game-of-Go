
x, y = 275, 275
matrix_cord_trans = []
for i in range(9):
    for k in range(9):
        matrix_cord_trans.append((x, y))
        x += 35
    y += 35
    x = 275

print(len(matrix_cord_trans))