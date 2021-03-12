n = int(input())
even = set()
odd = set()
for i in range(1,n+1):
    sum = 0
    name = input()
    for char in name:
        sum += ord(char)
    sum = int(sum/i)
    if sum % 2 == 0:
        even.add(sum)
    else:
        odd.add(sum)
even_sum = 0
odd_sum = 0
for num in even:
    even_sum += num
for num in odd:
    odd_sum += num
if even_sum == odd_sum:
    result = odd|even
    print(f"{', '.join(str(x) for x in result)}")
elif even_sum > odd_sum:
    result = odd^even
    print(f"{', '.join(str(x) for x in result)}")
elif odd_sum > even_sum:
    result = odd-even
    print(f"{', '.join(str(x) for x in result)}")