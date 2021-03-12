from collections import deque
dec = deque()
count_enque, count_deque, searched_element = [int(i) for i in input().split(" ")]
nums = [int(i) for i in input().split(" ")]
[dec.append(nums[i]) for i in range(count_enque)]
[dec.popleft() for i in range(count_deque)]
if searched_element in dec:
    print("True")
else:
    if dec:
        print(min(dec))
    else:
        print(0)