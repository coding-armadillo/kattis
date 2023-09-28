c = list(input())
s = input().split()
if len(c) != len(s):
    print("False")
else:
    d, valid = {}, True
    for a, b in zip(c, s):
        if a not in d:
            d[a] = b
        else:
            if d[a] != b:
                print("False")
                valid = False
                break
    if valid:
        if len(set(d.keys())) == len(set(d.values())):
            print("True")
        else:
            print("False")
