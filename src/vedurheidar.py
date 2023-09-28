v = int(input())
for _ in range(int(input())):
    s, k = input().split()
    if int(k) >= v:
        print(s, "opin")
    else:
        print(s, "lokud")
