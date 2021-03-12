count, length = input().split(", ")
count = int(count)
length = int(length)
matrix = []
for i in range(count):
    data = []
    command = input().split(" ")
    for j in range(length):
        data.append(int(command[j]))
    matrix.append(data)
for i in range(length):
    sum = 0
    for j in range(count):
        sum += matrix[j][i]
    print(sum)