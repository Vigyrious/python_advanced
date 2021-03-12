n = int(input())
matrix = [[int(i) for i in input().split(" ")] for _ in range(n)]
command = input()


def math(info):
    action, idx1, idx2, idx3 = info.split(" ")
    idx1, idx2 = int(idx1), int(idx2)
    if 0 <= idx1 < n and 0 <= idx2 < n:
        return True
    return False


while command != "END":
    if math(command):
        action, idx1, idx2, idx3 = command.split(" ")
        idx1, idx2, idx3 = int(idx1), int(idx2), int(idx3)
        if action == "Add":
            matrix[idx1][idx2] += idx3
        else:
            matrix[idx1][idx2] -= idx3
    else:
        print("Invalid coordinates")
    command = input()
[print(*sub) for sub in matrix]