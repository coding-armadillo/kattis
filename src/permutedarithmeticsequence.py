def arithmetic(n):
    d = [n[i] - n[i + 1] for i in range(len(n) - 1)]
    return True if len(set(d)) == 1 else False


for _ in range(int(input())):
    s = input().split()
    n = [int(d) for d in s[1:]]
    if arithmetic(n):
        print("arithmetic")
    elif arithmetic(sorted(n)):
        print("permuted arithmetic")
    else:
        print("non-arithmetic")
