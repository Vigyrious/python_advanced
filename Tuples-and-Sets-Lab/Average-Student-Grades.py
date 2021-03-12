iters = int(input())
dect = {}
for i in range(iters):
    name, grade = input().split(" ")
    grade = float(grade)
    if name not in dect:
        dect[name] = []
    dect[name].append(f"{grade:.2f}")
for key, value in dect.items():
    print(f"{key} -> {' '.join(str(x) for x in value)} (avg: {sum(float(i) for i in value)/len(value):.2f})")
