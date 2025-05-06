_ = input()
s1 = sum(int(d) for d in input().split())
s2 = sum(int(d) for d in input().split())
if s1 > s2:
    print("Button 1")
elif s1 < s2:
    print("Button 2")
else:
    print("Oh no")
