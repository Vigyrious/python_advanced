
def is_valid(num):
    result = [x for x in range(2,11) if num % x == 0]
    return result


print([i for i in range(int(input()), int(input()) +1) if is_valid(i)])