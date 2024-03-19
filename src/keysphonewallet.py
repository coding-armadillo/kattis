n = int(input())
items = [input() for _ in range(n)]
ready = True
for item in ["keys", "phone", "wallet"]:
    if item not in items:
        print(item)
        ready = False
if ready:
    print("ready")
