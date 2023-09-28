n = int(input())
w = input()

for i in range(n):
    a = f"{n-i} bottle{'s' if n-i >1 else ''}"
    b = f"{'no more' if n-i-1==0 else n-i-1 } bottle{'' if n-i-1==1 else 's'}"
    c = f"{'one' if n-i>1 else 'it' }"
    d = f"{' on the wall' if n-i-1 else ''}"
    print(f"{a} of {w} on the wall, {a} of {w}.")
    print(f"Take {c} down, pass it around, {b} of {w}{d}.")
    if n - i - 1:
        print()
