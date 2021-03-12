command = input().split("-")
dect = {}
while len(command) > 1:
    name, number = command
    if name not in dect:
        dect[name] = 0
    dect[name] = number
    command = input().split("-")
for i in range(int(command[0])):
    check_name = input()
    if check_name in dect:
        print(f"{check_name} -> {dect[check_name]}")
    else:
        print(f"Contact {check_name} does not exist.")