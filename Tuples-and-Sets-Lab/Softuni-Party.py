rotas = int(input())
dect = {}
for i in range(rotas):
    dect[input()] = 0
data = input()
while data != "END":
    if data in dect:
        dect.pop(data)
    data = input()
print(len(dect))
for key in sorted(dect.keys()):
    print(key)
