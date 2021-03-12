from collections import deque
s = deque()
def supermarket(command, s):
    if command != "Paid":
        s.append(command)
    else:
        while s:
            print(s.popleft())
    return s


def execute():
    global s
    command = input()
    while command != "End":
        s = supermarket(command,s)
        command = input()
    print(f"{len(s)} people remaining.")

execute()

