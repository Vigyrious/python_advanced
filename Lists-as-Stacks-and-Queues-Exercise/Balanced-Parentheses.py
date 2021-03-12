s = []
data = input()
is_balance = True
dect = {"(": ")", "{": "}", "[": "]"}
for char in data:
    if char in "({[":
        s.append(char)
    elif char in ")}]":
        if s:
            current = s.pop()
            if char == dect[current]:
                continue
            else:
                is_balance = False
                break
        else:
            is_balance = False
            break
if is_balance:
    print("YES")
else:
    print("NO")