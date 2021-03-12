from collections import deque
cups = deque(int(i) for i in input().split(" "))
bottles = [int(i) for i in input().split(" ")]
filled = True
wasted = 0
addition = ""
while bottles and cups:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()
    if current_bottle >= current_cup:
        wasted += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        while current_cup>0 and bottles:
            current_bottle = bottles.pop()
            current_cup -= current_bottle
            if current_cup <= 0:
                wasted += abs(current_cup)
        if current_cup > 0:
            addition += str(current_cup)+" "
            break
if not cups:
    bottles = bottles[::-1]
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
else:
    print(f"Cups: {addition+' ' if addition else ''}{' '.join([str(x) for x in cups])}")
print(f"Wasted litters of water: {wasted}")