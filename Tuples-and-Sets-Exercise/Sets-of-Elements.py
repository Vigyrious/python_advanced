len1, len2 = input().split(" ")
len1, len2 = int(len1), int(len2)
set1 = {input() for i in range(len1)}
set2 = {input() for i in range(len2)}
for nums in set1&set2:
    print(nums)