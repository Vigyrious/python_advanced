def even(x):
    return x % 2 == 0


def solve(data):
    return list(filter(even, data))



print(solve([int(i) for i in input().split(" ")]))

