categories = {k: {} for k in input().split(", ")}
for i in range(int(input())):
    categorie, item, combine = input().split(" - ")
    quant, qual = combine.split(";")[0].split(":")[1], combine.split(";")[1].split(":")[1]
    categories[categorie][item] = [[quant],[qual]]
items_count = [[int(i) for i in categories[name][item][0]] for name in categories for item in categories[name]]
quality_count = [[int(i) for i in categories[name][item][1]] for name in categories for item in categories[name]]
print(f"Count of items: {sum([int(i) for sub in items_count for i in sub])}\nAverage quality: {sum([int(i) for sub in quality_count for i in sub]) / len(categories):.2f}")
[print(f"{categorie} -> {', '.join([i for i in categories[categorie]])}") for categorie in categories]