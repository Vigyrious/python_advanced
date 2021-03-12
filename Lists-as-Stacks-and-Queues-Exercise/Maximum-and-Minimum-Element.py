s = []
iters = int(input())
for i in range(iters):
    command = input().split(" ")
    if len(command) > 1:
        s.append(int(command[1]))
    else:
        command = int(command[0])
        if command == 2:
            if s:
                s.pop()
        elif command == 3:
            if s:
                print(max(s))
        else:
            if s:
                print(min(s))
s = [str(i) for i in s]
print(', '.join(s[::-1]))