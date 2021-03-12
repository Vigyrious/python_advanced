count, length = input().split(", ")
matrix = []
for _ in range(int(count)):
    data = []
    nums = input().split(", ")
    for i in range(int(length)):
        data.append(int(nums[i]))
    matrix.append(data)
print(sum([int(i) for i in subzame for subzame in matrix]))
print(matrix)