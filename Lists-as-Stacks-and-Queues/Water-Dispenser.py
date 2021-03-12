from collections import deque
s = deque()


def execute(dispenser, s):
    dispenser = int(dispenser)
    command = input()
    while command != "Start":
        s.append(command)
        command = input()
    command = input()
    while command != "End":
        current = command.split(" ")
        if len(current) > 1:
            dispenser += int(current[1])
        else:
            current_needed = int(current[0])
            if dispenser >= current_needed:
                print(f"{s.popleft()} got water")
                dispenser -= current_needed
            else:
                print(f"{s.popleft()} must wait")
        command = input()
    print(f"{dispenser} liters left")


execute(int(input()), s)