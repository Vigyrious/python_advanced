from math import log,e
n = int(input())
logs = input()
if logs == "natural":
    print(f"{log(n,e):.2f}")
else:
    print(f"{log(n,int(logs)):.2f}")