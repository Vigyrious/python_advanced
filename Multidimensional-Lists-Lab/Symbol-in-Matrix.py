n = int(input())
matrix = []
for i in range(n):
    matrix.append(input().split(" "))
symbol = input()
location = []
for i in range(len(matrix)):
    for k in range(len(matrix[i])):
        print(matrix[i][k])
        if symbol in matrix[i][k]:
            print("True")
if location:
    print(*location)
else:
    print(f"{symbol} does not occur in the matrix")