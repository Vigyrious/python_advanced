def combinations(values, k, comb=[]):
    # indent = " "*len(comb)
    if len(comb) == k:
        print(', '.join(comb))
        return
    for i in range(len(values)):
        x = values[i]
        comb.append(x)
        # print(indent+"+"+str(x))
        combinations(values[i+1:], k, comb)
        # print(indent+"-"+str(x))
        comb.pop()


combinations([i for i in input().split(", ")],int(input()))