n = int(input())
D_s = input()

stack = []

valid = True

for i in range(n):
    c = D_s[i]
    if c in ["(", "[", "{"]:
        stack.append(c)
    if c in [")", "]", "}"]:
        if len(stack) == 0:
            valid = False
            break
        v = stack.pop()
        if c == ")" and v != "(":
            valid = False
            break
            
        elif c == "]" and  v != "[":
            valid = False
            break
            
        elif c == "}" and  v != "{":
            valid = False
            break

if valid:
    print("ok so far")
else:
    print(c, i)
