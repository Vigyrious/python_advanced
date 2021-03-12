string = input()
dect = {}
for char in string:
    if char not in dect:
        dect[char] = 0
    dect[char] += 1
for key, value in sorted(dect.items()):
    print(f"{key}: {value} time/s")