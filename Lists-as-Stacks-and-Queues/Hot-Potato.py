from collections import deque


def solve():
    s = deque(input().split(" "))
    # [s.append(i) for i in input().split()]
    throws = int(input())
    while len(s) > 1:
        for i in range(1, throws+1):
            person = s.popleft()
            if i == throws:
                print(f"Removed {person}")
            else:
                s.append(person)
    print(f"Last is {s.popleft()}")

solve()