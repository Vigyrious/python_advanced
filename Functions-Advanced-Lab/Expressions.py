
def find_count(numbers, sum=0, expression=""):
    if not numbers:
        return [(expression, sum)]

    result_plus = find_count(numbers[1:], sum+int(numbers[0]), expression + f"+{numbers[0]}")
    result_minus = find_count(numbers[1:], sum-int(numbers[0]), expression + f"-{numbers[0]}")
    return result_plus + result_minus


result = find_count([int(i) for i in input().split(", ")])
[print(f"{exp}={res}") for exp, res in result]
