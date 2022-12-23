set_num = 0
while True:
    size = int(input())
    if size == 0:
        break

    names = []
    for _ in range(size):
        names.append(input())

    set_num += 1
    print(f"SET {set_num}")

    top, bottom = [], []
    for i in range(1, size, 2):
        bottom.append(names[i])
    for i in range(0, size, 2):
        top.append(names[i])
    names = top + bottom[::-1]
    for name in names:
        print(name)
