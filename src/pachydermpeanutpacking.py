def inbox(coords, x, y):
    if x >= coords[0] and x <= coords[2] and y >= coords[1] and y <= coords[3]:
        return True
    return False


while True:
    n = int(input())
    if not n:
        break
    box = {}
    for i in range(n):
        desc = input().split()
        size = desc[-1]
        coords = [float(d) for d in desc[:-1]]
        box[i] = (coords, size)
    m = int(input())
    for _ in range(m):
        desc = input().split()
        size = desc[-1]
        x, y = [float(d) for d in desc[:-1]]
        floor = True
        for i in range(n):
            coords, box_size = box[i]
            if inbox(coords, x, y):
                floor = False
                break
        if floor:
            status = "floor"
        else:
            status = "correct" if box_size == size else box_size
        print(size, status)
    print()
