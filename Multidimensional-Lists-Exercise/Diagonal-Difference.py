matrix = []
def solve(matrix):
    primary = 0
    seconday = 0
    secondary_first = len(matrix) - 1
    for i in range(len(matrix)):
        primary += matrix[i][i]
        seconday += matrix[i][secondary_first]
        secondary_first -= 1
    return abs(primary - seconday)




def create_matrix(data):
    matrix.append(list(data))
    return matrix


def execute(n):
    [create_matrix(list(map(int,input().split(" ")))) for _ in range(n)]
    print(solve(matrix))


execute(int(input()))