w = input()
b, k = w.count("b"), w.count("k")
if not b and not k:
    print("none")
elif b == k:
    print("boki")
elif b > k:
    print("boba")
else:
    print("kiki")
