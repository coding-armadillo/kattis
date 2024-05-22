n, k = input().split()
a = input().split()
ind = a.index(k)
if ind == 0:
    print("fyrst")
elif ind == 1:
    print("naestfyrst")
else:
    print(ind + 1, "fyrst")
