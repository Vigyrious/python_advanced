def permutations(idx,values):
    if idx == len(values):
        print(''.join(values))
        return
    for i in range(idx,len(values)):
        values[idx], values[i] = values[i],values[idx]
        permutations(idx+1,values)
        values[idx], values[i] = values[i],values[idx]


permutations(0, list(input()))