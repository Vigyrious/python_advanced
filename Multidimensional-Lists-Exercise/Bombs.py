n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(i) for i in input().split(" ")])
bombs = input().split(" ")


def damage(m,row,col):
    bomb_damage = m[row][col]
    if row - 1 >= 0:
        if m[row-1][col] > 0:
            m[row-1][col] -= bomb_damage
    if row - 1 >= 0 and col - 1 >= 0:
        if m[row-1][col-1] > 0:
            m[row-1][col-1] -= bomb_damage
    if row - 1 >= 0 and col + 1 < len(m):
        if m[row-1][col+1] > 0:
            m[row-1][col+1] -= bomb_damage
    if row + 1 < len(matrix):
        if m[row+1][col] > 0:
            m[row+1][col] -= bomb_damage
    if row + 1 < len(matrix) and col - 1 >= 0:
        if m[row+1][col-1] > 0:
            m[row+1][col-1] -= bomb_damage
    if row + 1 < len(matrix) and col + 1 < len(matrix):
        if m[row+1][col+1] > 0:
            m[row+1][col+1] -= bomb_damage
    if col - 1 >= 0:
        if m[row][col-1] > 0:
            m[row][col-1] -= bomb_damage
    if col + 1 < len(matrix):
        if m[row][col+1] > 0:
            m[row][col+1] -= bomb_damage
    m[row][col] = 0
    return m



while bombs:
    bomb=bombs.pop(0)
    bomb = bomb.split(",")
    bomb_row, bomb_col = map(int,bomb)
    if matrix[bomb_row][bomb_col] > 0:
        matrix = damage(matrix, bomb_row, bomb_col)
survived = []
for i in range(len(matrix)):
    for char in matrix[i]:
        if char > 0:
            survived.append(char)
print(f"Alive cells: {len(survived)}")
print(f"Sum: {sum([int(i) for i in survived])}")
[print(*sub) for sub in matrix]