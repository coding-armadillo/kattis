for _ in range(int(input())):
    command = input()
    start = "Simon says "
    if command.startswith(start):
        print(command[len(start) :])
