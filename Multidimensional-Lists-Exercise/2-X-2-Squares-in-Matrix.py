rows, cols = map(int, input().split(" "))
matrix = []

def checker(max, rol, col):
    count = 0
    for i in range(rol-1):
        for k in range(col-1):
            maze = [max[i][k],max[i][k+1],max[i+1][k],max[i+1][k+1]]
            if maze.count(maze[0]) == 4:
                count += 1
    return count



def execute(row,col):
    [matrix.append([i for i in input().split(" ")]) for _ in range(row)]
    print(checker(matrix, row, col))


execute(rows, cols)