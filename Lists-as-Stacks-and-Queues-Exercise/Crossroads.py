green_light = int(input())
free_window = int(input())
from collections import deque
d = deque()
has_crashed = False
safe = False
total = 0
while not has_crashed:
    command = input()
    while command != "green" and command != "END":
        d.append(command)
        command = input()
    if command == "END":
        break
    if d:
        last_car = d.popleft()
        current = deque([i for i in last_car])
        total += 1
    else:
        break
    for i in range(green_light):
        if current:
            current.popleft()
        else:
            if d:
                last_car = d.popleft()
                current = deque([i for i in last_car])
                total += 1
                current.popleft()
            else:
                break
    if current:
        for i in range(free_window):
            if current:
                current.popleft()
            else:
                break
    if current:
        has_crashed = True
        print("A crash happened!")
        print(f"{last_car} was hit at {current.popleft()}.")
        break
if not has_crashed:
    print("Everyone is safe.")
    print(f"{total} total cars passed the crossroads.")