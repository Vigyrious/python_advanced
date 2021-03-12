
def create_matrix(row):
    matrix = []
    [matrix.append(list(map(int,input().split()))) for _ in range(row)]
    return matrix

def math(maze):
    sum = 0
    for submaze in maze:
        for item in submaze:
            sum += item
    return sum


def solve(row_count, col_count):
    largest = None
    largest_maze = []
    matrix = create_matrix(row_count)
    for row in range(row_count-2):
        for col in range(col_count-2):
            maze = [
                [matrix[row][col], matrix[row][col+1],matrix[row][col+2]],
                [matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]],
                [matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]
            ]
            current_sum = math(maze)
            if largest is not None:
                if current_sum > largest:
                    largest = current_sum
                    largest_maze = maze
            else:
                largest = current_sum
                largest_maze = maze
    return (largest, largest_maze)


row, col = map(int,input().split(" "))
answer = solve(row, col)
print(f"Sum = {answer[0]}")
for sub in answer[1]:
    print(*sub)