names = [i for i in input().split(", ")]
command = input()
dect = {k:{} for k in names}
while command != "End":
    name, weapon, quant = command.split("-")
    if name in dect:
        if weapon not in dect[name]:
            dect[name][weapon] = int(quant)

    command = input()
[print(f"{name} -> Items: {len(dect[name])}, Cost: {sum(dect[name].values())}") for name in dect]