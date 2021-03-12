def solve(data):
    return (min(data),max(data),sum(data))


result = solve([int(i) for i in input().split(" ")])

print(f"The minimum number is {result[0]}")
print(f"The maximum number is {result[1]}")
print(f"The sum number is: {result[2]}")