

def solve(data):
    negative = -sum([abs(int(i)) for i in data if i < 0])
    positive = sum([int(i) for i in data if i > 0])
    return (negative, positive, f"The negatives are stronger than the positives" if abs(negative) > positive else "The positives are stronger than the negatives")

[print(sub) for sub in solve([int(i) for i in input().split(" ")])]