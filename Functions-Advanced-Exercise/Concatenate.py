def concatenate(*args):
    str = ""
    for word in args:
        str += word
    return str


print(concatenate("Soft", "Uni", "Is", "Great", "!"))