_, p, s = input().split()
for _ in range(int(s)):
    if p in input().split()[1:]:
        print("KEEP")
    else:
        print("REMOVE")
