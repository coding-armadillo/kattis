input()
l = sum([int(d) for d in input().split()])
r = sum([int(d) for d in input().split()])

if l == r:
    print("either")
elif l < r:
    print("left")
else:
    print("right")
