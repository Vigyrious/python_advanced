command = input()
data = [int(i) for i in input().split(" ")]


def solve(command, data):
    return sum([i for i in data if i % 2 != 0]) * len(data) if command == "Odd" else sum([i for i in data if i % 2 == 0]) * len(data)



print(solve(command, data))