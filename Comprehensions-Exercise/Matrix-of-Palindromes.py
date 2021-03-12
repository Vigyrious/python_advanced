r, c = map(int, input().split(" "))

[print(' '.join([f"{chr(97+row)}{chr(97+row+col)}{chr(97+row)}" for col in range(c)])) for row in range(r)]