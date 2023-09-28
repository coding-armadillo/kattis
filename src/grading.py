line = input()
score = int(input())
a, b, c, d, e = [int(d) for d in line.split()]
if score >= a:
    print("A")
elif score >= b:
    print("B")
elif score >= c:
    print("C")
elif score >= d:
    print("D")
elif score >= e:
    print("E")
else:
    print("F")
