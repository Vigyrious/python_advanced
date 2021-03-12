split_counts = [int(i) for i in input().split(" ")]
count_push = split_counts[0]
count_pop = split_counts[1]
element = int(split_counts[2])
s = []
nums = input().split(" ")
[s.append(int(nums[i])) for i in range(count_push)]
[s.pop() for i in range(count_pop)]
if element in s:
    print("True")
else:
    print(min(s))
