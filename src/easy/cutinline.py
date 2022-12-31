n = int(input())
queue = []
for _ in range(n):
    queue.append(input())

c = int(input())
for _ in range(c):
    event = input().split()
    if event[0] == "leave":
        queue.remove(event[1])
    elif event[0] == "cut":
        queue.insert(queue.index(event[2]), event[1])

for name in queue:
    print(name)
