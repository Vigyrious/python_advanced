matrix = []
row, col = map(int, input().split(" "))
from collections import deque
snake = deque(input())
[matrix.append(["None"for i in range(col)]) for _ in range(row)]
row_index = 0
col_index = 0
snake_copy = deque(snake)
forward = True
while True:
    current_letter = snake.popleft()
    snake.append(current_letter)
    matrix[row_index][col_index] = current_letter
    if forward:
        col_index += 1
    else:
        col_index -= 1
    if col_index == col and row_index == row - 1 or col_index == -1 and row_index == row - 1:
        break
    if col_index == len(matrix[0]) and row_index+1 < row:
        forward = False
        row_index += 1
        col_index = len(matrix[0]) - 1
    if col_index < 0 and row_index+1 < row:
        row_index += 1
        forward = True
        col_index = 0
for sub in matrix:
    print(''.join(sub))
