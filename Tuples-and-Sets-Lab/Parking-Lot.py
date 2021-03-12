rotas = int(input())
dect = {}
for i in range(rotas):
    action, serial = input().split(", ")
    if action == "IN":
        if serial not in dect:
            dect[serial] = 0
    elif action == "OUT":
        if serial in dect:
            dect.pop(serial)
if dect:
    for key in dect.keys():
        print(key)
else:
    print("Parking Lot is Empty")