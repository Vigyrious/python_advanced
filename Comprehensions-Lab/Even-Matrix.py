# n = int(input())
print([[i for i in sub if i % 2 == 0] for sub in [[int(i) for i in input().split(", ")] for _ in range(int(input()))]])