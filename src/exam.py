k = int(input())
y = input()
f = input()
same, different = 0, 0
for a, b in zip(y, f):
    if a == b:
        same += 1
    else:
        different += 1
print(min(same, k) + min(different, (len(y) - k)))
