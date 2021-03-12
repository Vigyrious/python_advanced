def get_expressions(expression):
    opening_stack = []
    current_expressions = []
    for i in range(len(expression)):
        char = expression[i]
        if char == "(":
            opening_stack.append(i)
        elif char == ")":
            start = opening_stack.pop()
            end = i
            current_expressions.append(expression[start:end+1])
    return current_expressions


sub_expressions = get_expressions(input())
[print(exp) for exp in sub_expressions]