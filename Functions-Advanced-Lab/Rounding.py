def rounding(list):
    return [round(float(i)) for i in list]


print(rounding([i for i in input().split(" ")]))