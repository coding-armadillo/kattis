while True:
    room_x, room_y = [int(d) for d in input().split()]
    if not room_x and not room_y:
        break

    robot_x, robot_y = 0, 0
    actual_x, actual_y = 0, 0

    n = int(input())
    for _ in range(n):
        direction, step = input().split()
        step = int(step)

        if direction == "u":
            robot_y += step
            actual_y = min(room_y - 1, actual_y + step)
        elif direction == "d":
            robot_y -= step
            actual_y = max(0, actual_y - step)
        elif direction == "r":
            robot_x += step
            actual_x = min(room_x - 1, actual_x + step)
        elif direction == "l":
            robot_x -= step
            actual_x = max(0, actual_x - step)

    print(f"Robot thinks {robot_x} {robot_y}")
    print(f"Actually at {actual_x} {actual_y}")
    print()
