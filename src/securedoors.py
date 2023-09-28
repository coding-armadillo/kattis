pool = set()
for _ in range(int(input())):
    action, name = input().split()
    if action == "entry":
        print(name, "entered", "(ANOMALY)" if name in pool else "")
        pool.add(name)
    elif action == "exit":
        print(name, "exited", "(ANOMALY)" if name not in pool else "")
        pool.discard(name)
