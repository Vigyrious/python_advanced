def multiply(*args):
    mult = 1
    data = [int(i) for i in args]
    for num in data:
        mult *= num
    return mult

print(multiply(1, 4, 5))