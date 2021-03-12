bullet_price = int(input())
barrel_size = int(input())
from collections import deque
bullets = [int(i) for i in input().split(" ")]
locks = deque([int(i) for i in input().split(" ")])
value = int(input())
bullet_size = len(bullets)
reload = 0
while True:
    while bullets and locks:
        current_bullet = bullets.pop()
        current_lock = locks.popleft()
        if current_bullet <= current_lock:
            if reload == barrel_size:
                print("Reloading!")
                reload = 0
            print("Bang!")
            reload += 1
            continue
        else:
            if reload == barrel_size:
                print("Reloading!")
                reload = 0
            print("Ping!")
            reload += 1
            if bullets:
                current_bullet = bullets.pop()
                while current_bullet > current_lock:
                    if reload == barrel_size:
                        print("Reloading!")
                        reload = 0
                    print("Ping!")
                    reload += 1
                    if bullets:
                        current_bullet = bullets.pop()
                    else:
                        locks.append(current_lock)
                        break
                if current_bullet <= current_lock:
                    if reload == barrel_size:
                        print("Reloading!")
                        reload = 0
                    print("Bang!")
                    reload += 1
                continue
    if reload == barrel_size and bullets:
        print("Reloading!")
    break
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    left = bullet_size - len(bullets)
    earned = 0 if bullet_price == 0 else left*bullet_price
    print(f"{len(bullets)} bullets left. Earned ${value - earned:.0f}")
