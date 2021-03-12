from collections import deque
rotas = int(input())
d = deque()
for _ in range(rotas):
    splitted = input().split(" ")
    petrol = int(splitted[0])
    distance = int(splitted[1])
    d.append((petrol, distance))
is_right = False
starting_point = 0
capacity = 0
while not is_right:
    new_d = deque(d)
    for i in range(len(new_d)):
        petrol, distance = new_d.popleft()
        capacity += petrol
        if capacity < distance:
            d.popleft()
            capacity = 0
            starting_point += 1
            break
        else:
            capacity -= distance
        if not new_d:
            is_right = True
            break
print(starting_point)
