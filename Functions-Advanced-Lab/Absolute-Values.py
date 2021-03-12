def abs_values(list):
    return [abs(float(i)) for i in list]

print(abs_values([i for i in input().split(" ")]))