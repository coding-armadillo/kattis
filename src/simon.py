for _ in range(int(input())):
    command = input()
    start = "simon says "
    if command.startswith(start):
        print(command[len(start) :])
    else:
        print()
