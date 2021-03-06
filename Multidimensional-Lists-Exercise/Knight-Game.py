row = int(input())
matrix = []
[matrix.append(list(input()))for _ in range(row)]
col = row
current_damage = 0
position = []
removed = 0
def total_damage(matrix,row,col):
    count = 0
    if row - 2 >= 0 and col - 1 >= 0:
        if matrix[row-2][col-1] == "K":
            count += 1
    if row - 2 >= 0 and col + 1 < len(matrix):
        if matrix[row-2][col+1] == "K":
            count += 1
    if row + 2 < len(matrix) and col + 1 < len(matrix):
        if matrix[row+2][col+1] == "K":
            count += 1
    if row + 2 < len(matrix) and col - 1 >= 0:
        if matrix[row+2][col-1] == "K":
            count += 1
    if col - 2 >= 0 and row + 1 < len(matrix):
        if matrix[row+1][col-2] == "K":
            count += 1
    if col - 2 >= 0 and row - 1 >= 0:
        if matrix[row-1][col-2] == "K":
            count += 1
    if col + 2 < len(matrix) and row + 1 < len(matrix):
        if matrix[row+1][col+2] == "K":
            count += 1
    if col + 2 < len(matrix) and row - 1 >= 0:
        if matrix[row-1][col+2] == "K":
            count += 1
    return count



while True:
    for row_index in range(row):
        for col_index in range(col):
            if matrix[row_index][col_index] == "K":
                calculated_damage = total_damage(matrix,row_index,col_index)
                if calculated_damage > current_damage:
                    current_damage = calculated_damage
                    position = [row_index,col_index]
    if current_damage == 0:
        break
    else:
        matrix[position[0]][position[1]] = "0"
        current_damage = 0
        removed += 1
        position = []
print(removed)

