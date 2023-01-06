from itertools import product

ops = ["+", "-", "*", "//"]

for _ in range(int(input())):
    s = int(input())
    solved = False
    for op1, op2, op3 in product(ops, ops, ops):
        e = f"4 {op1} 4 {op2} 4 {op3} 4"
        try:
            ans = eval(e) == s
        except:
            ans = False
        if ans:
            print(f"{e.replace('//','/')} = {s}")
            solved = True
            break
    if not solved:
        print("no solution")
