def even_odd(*args):
    data = [i for i in args]
    command = data.pop()
    return [i for i in data if int(i) % 2 == 0] if command == "even" else [i for i in data if int(i) % 2 != 0]



print(even_odd(1, 2, 3, 4, 5, 6, "even"))