class NameTooShort(Exception):
    def __init__(self):
        self.message = "Name must be more than 4 characters"

    def __str__(self):
        return self.message


class MustContainASymbol(Exception):
    def __init__(self):
        self.message = "Email must contain @"

    def __str__(self):
        return self.message


class InvalidDomain(Exception):
    def __init__(self):
        self.message = "Domain must be one of the following: .com, .bg, .org, .net"

    def __str__(self):
        return self.message


email = input()
domains = ["com","bg","org","net"]

while email != "End":
    if "@" not in email:
        raise MustContainASymbol
    name, domain = email.split("@")[0], email.split("@")[1]
    if len(name) < 5:
        raise NameTooShort
    domain_ext = domain.split(".")
    if domain_ext[1] not in domains:
        raise InvalidDomain
    print("Email is valid")
    email = input()
