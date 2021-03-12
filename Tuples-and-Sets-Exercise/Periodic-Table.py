n = int(input())
set1 = set()
for i in range(n):
    splitted = input().split(" ")
    for word in splitted:
        set1.add(word)
for element in set1:
    print(element)