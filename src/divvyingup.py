_ = input()
p = [int(d) for d in input().split()]
if sum(p) % 3:
    print("no")
else:
    print("yes")
