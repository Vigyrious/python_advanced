n = int(input())
commands = input().split(" ")
maze = []
[maze.append([i for i in input().split(" ")]) for _ in range(n)]
position = [[row, col] for row in range(len(maze)) for col in range(len(maze[0])) if maze[row][col] == "s"]
position = position.pop()
coals = sum([sub.count("c") for sub in maze])
coal = 0
has_won = False
has_exploded = False
while commands:
    row, col = position[0], position[1]
    current_command = commands.pop(0)
    length = len(maze)
    if current_command == "up" and row-1 in range(length):
            if maze[row-1][col] == "c":
                coal += 1
            elif maze[row-1][col] == "e":
                has_exploded = True
                position[0] = row-1
                break
            maze[row][col], maze[row-1][col] = "*", "s"
            position[0] = row - 1
    elif current_command == "down" and row + 1 in range(length):
            if maze[row + 1][col] == "c":
                coal += 1
            elif maze[row + 1][col] == "e":
                has_exploded = True
                position[0] = row + 1
                break
            maze[row][col], maze[row+1][col] = "*", "s"
            position[0] = row + 1
    elif current_command == "left" and col - 1 in range(length):
            if maze[row][col-1] == "c":
                coal += 1
            elif maze[row][col-1] == "e":
                has_exploded = True
                position[1] = col-1
                break
            maze[row][col], maze[row][col-1] = "*", "s"
            position[1] = col - 1
    elif current_command == "right" and col + 1 in range(length):
            if maze[row][col+1] == "c":
                coal += 1
            elif maze[row][col+1] == "e":
                has_exploded = True
                position[1] = col + 1
                break
            maze[row][col], maze[row][col+1] = "*", "s"
            position[1] = col + 1
    if coal == coals:
        has_won = True
        break
if has_won:
    print(f"You collected all coals! ({position[0]}, {position[1]})")
elif has_exploded:
    print(f"Game over! ({position[0]}, {position[1]})")
else:
    print(f"{coals - coal} coals left. ({position[0]}, {position[1]})")