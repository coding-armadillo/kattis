from itertools import product

a, b, c, d = [int(d) for d in input().split()]
ops = ["*", "+", "-", "//"]
valid = False
for op1, op2 in product(ops, ops):
    e = f"{a} {op1} {b} == {c} {op2} {d}"
    try:
        if eval(e):
            print(e.replace("==", "=").replace("//", "/"))
            valid = True
    except:
        pass
if not valid:
    print("problems ahead")
