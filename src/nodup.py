words = input().split()

counter = {}
repeated = False
for w in words:
    if w in counter:
        repeated = True
        break
    else:
        counter[w] = None
if repeated:
    print("no")
else:
    print("yes")
