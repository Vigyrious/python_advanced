s = [int(i) for i in input().split(" ")]
capacity = int(input())
count = 0
racks = 1
while s:
    last = s.pop()
    if count + last <= capacity:
        count += last
    else:
        racks += 1
        count = last
print(racks)