a, op, b = input(), input(), input()
pa, pb = a.count("0"), b.count("0")
if op == "*":
    print(f"1{'0'*(pa+pb)}")
elif op == "+":
    if pa == pb:
        ans = f"2{'0'*pa}"
    else:
        ans = f"1{'0'*(abs(pa-pb)-1)}1{'0'*min(pa,pb)}"
    print(ans)
