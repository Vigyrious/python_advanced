def operate(*args):
    operator, *numbers = args
    numbers = [int(i) for i in numbers]
    result = None
    if operator == "+":
        return sum([int(i) for i in numbers])
    elif operator == "-":
        result = numbers.pop(0)
        for num in numbers:
            result -= num
        return result
    elif operator == "*":
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operator == "/":
        result = numbers.pop(0)
        for num in numbers:
            result /= num
        return result

print(operate("*", 3, 4))