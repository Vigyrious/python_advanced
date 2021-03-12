def age_assignment(*args, **kwargs):
    dect = {}
    for name in args:
        for letter, age in kwargs.items():
            if name.startswith(letter):
                dect[name] = age
    return dect


print(age_assignment("Peter", "George", G=26, P=19))