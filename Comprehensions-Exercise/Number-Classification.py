data = [int(i) for i in input().split(", ")]
print(f"Positive: {', '.join([str(i) for i in data if i >= 0])}\nNegative: {', '.join([str(k) for k in data if k < 0])}\nEven: {', '.join([str(e) for e in data if e % 2 == 0])}\nOdd: {', '.join([str(n) for n in data if n % 2 != 0])}")