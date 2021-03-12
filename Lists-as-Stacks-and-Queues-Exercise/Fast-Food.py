from collections import deque
quantity = int(input())
d = deque([int(i) for i in input().split(" ")])
if d:
    print(max(d))
for i in range(len(d)):
    index = 0
    if quantity >= d[index]:
        quantity -= d[index]
        d.popleft()
    else:
        index += 1
if not d:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in d])}")