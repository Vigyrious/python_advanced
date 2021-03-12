data = input().split(" ")
sets = dict.fromkeys(data)
for key in sets:
    print(f"{float(key):.1f} - {data.count(key)} times")