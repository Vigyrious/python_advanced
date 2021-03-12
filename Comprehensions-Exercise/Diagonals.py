n = int(input())
matrix = [[int(i) for i in input().split(", ")] for _ in range(n)]
print(f"First diagonal: {', '.join([str(matrix[i][i]) for i in range(n)])}. Sum: {sum([matrix[i][i] for i in range(n)])}")
print(f"Second diagonal: {', '.join([str(matrix[i][j]) for i in range(n) for j in range(n) if i+j == n-1])}. Sum: {sum([matrix[i][j] for i in range(n) for j in range(n) if i+j == n-1])}")