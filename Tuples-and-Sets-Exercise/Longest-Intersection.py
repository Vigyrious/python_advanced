n = int(input())
largest = []
for _ in range(n):
    numbers = input().split("-")
    set1, set2 = numbers
    num1_start, num1_end = set1.split(",")
    num2_start, num2_end = set2.split(",")
    combo1 = {int(i) for i in range(int(num1_start), int(num1_end)+1)}
    combo2 = {int(i) for i in range(int(num2_start), int(num2_end) + 1)}
    intersection = combo1&combo2
    if len(intersection) > len(largest):
        largest = [i for i in intersection]
print(f"Longest intersection is {[int(i) for i in largest]} with length {len(largest)}")