row, col = map(int, input().split(" "))
matrix = []
[matrix.append(list(input())) for _ in range(row)]
movements = list(input())
player_row, player_col = [[row_index,col_index] for row_index in range(row) for col_index in range(col) if matrix[row_index][col_index] == "P"][0]
is_dead = False
has_won = False
while not is_dead and not has_won:
    bunnies = [[bunny_row, bunny_col] for bunny_row in range(row) for bunny_col in range(col) if matrix[bunny_row][bunny_col] == "B"]
    current_movement = movements.pop(0)
    if current_movement == "U":
        if player_row-1 in range(row):
            if matrix[player_row-1][player_col] == "B":
                player_row -= 1
                matrix[player_row][player_col] = "B"
                is_dead = True
            else:
                matrix[player_row][player_col] = "."
                matrix[player_row - 1][player_col] = "P"
                player_row -= 1
        else:
            matrix[player_row][player_col] = "."
            has_won = True
    elif current_movement == "D":
        if player_row+1 in range(row):
            if matrix[player_row+1][player_col] == "B":
                player_row += 1
                matrix[player_row][player_col] = "B"
                is_dead = True
            else:
                matrix[player_row][player_col] = "."
                matrix[player_row + 1][player_col] = "P"
                player_row += 1
        else:
            matrix[player_row][player_col] = "."
            has_won = True
    elif current_movement == "L":
        if player_col-1 in range(col):
            if matrix[player_row][player_col - 1] == "B":
                player_col -= 1
                matrix[player_row][player_col] = "B"
                is_dead = True
            else:
                matrix[player_row][player_col] = "."
                matrix[player_row][player_col - 1] = "P"
                player_col -= 1
        else:
            matrix[player_row][player_col] = "."
            has_won = True
    elif current_movement == "R":
        if player_col+1 in range(col):
            if matrix[player_row][player_col + 1] == "B":
                player_col += 1
                matrix[player_row][player_col] = "B"
                is_dead = True
            else:
                matrix[player_row][player_col] = "."
                matrix[player_row][player_col + 1] = "P"
                player_col += 1
        else:
            matrix[player_row][player_col] = "."
            has_won = True
    for bunny in bunnies:
        bunny_row, bunny_col = bunny
        if bunny_row+1 in range(row):
            if matrix[bunny_row+1][bunny_col] == "P":
                is_dead = True
            matrix[bunny_row + 1][bunny_col] = "B"
        if bunny_row-1 in range(row):
            if matrix[bunny_row-1][bunny_col] == "P":
                is_dead = True
            matrix[bunny_row - 1][bunny_col] = "B"
        if bunny_col + 1 in range(col):
            if matrix[bunny_row][bunny_col+1] == "P":
                is_dead = True
            matrix[bunny_row][bunny_col+1] = "B"
        if bunny_col - 1 in range(col):
            if matrix[bunny_row][bunny_col-1] == "P":
                is_dead = True
            matrix[bunny_row][bunny_col-1] = "B"
[print(''.join(sub)) for sub in matrix]
print(f"won: {player_row} {player_col}") if has_won else print(f"dead: {player_row} {player_col}")