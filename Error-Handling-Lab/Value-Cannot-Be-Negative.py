class ValueCannotBeNegative(Exception):
    pass

nums = []
for i in range(5):
    nums.append(int(input()))

for num in nums:
    if int(num) < 0:
        raise ValueCannotBeNegative

