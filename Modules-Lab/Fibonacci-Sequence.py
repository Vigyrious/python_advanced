from my_modules.modules import fibonacci, locate
command = input()
fibo = []
while command != "Stop":
    if "Create" in command:
        fibo = fibonacci(int(command.split(" ")[2]))
        print(' '.join(str(x) for x in fibo))
    else:
        print(locate(fibo, int(command.split(" ")[1])))
    command = input()