def create(row):
    matrix = []
    [matrix.append([i for i in input().split(" ")]) for _ in range(row)]
    return matrix

def swap(row1,col1,row2,col2, matrix):
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    return matrix


def solve(row,col):
    matrix = create(row)
    command = input()
    while command != "END":
        if len(command.split()) != 5:
            print("Invalid input!")
            command = input()
            continue
        action, row1, col1, row2, col2 = map(int,command.split(" "))
        if action == "swap":
            if 0 <= row1 < row and 0 <= row2 < row and 0 <= col1 < len(matrix[0]) and 0 <= col2 < len(matrix[0]):
                matrix = swap(row1,col1,row2,col2,matrix)
                [print(*sub) for sub in matrix]
            else:
                print("Invalid input!")
        command = input()



row, col = [int(i) for i in input().split(" ")]
solve(row,col)