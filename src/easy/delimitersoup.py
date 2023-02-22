n = int(input())
s = input()
stack = []
is_valid = True
for i in range(n):
    c = s[i]
    if c == " ":
        continue
    elif c in ["(", "[", "{"]:
        stack.append(c)
    else:
        if len(stack) == 0:
            is_valid = False
            break
        last = stack.pop()
        if c == ")" and last != "(":
            is_valid = False
            break
        if c == "]" and last != "[":
            is_valid = False
            break
        if c == "}" and last != "{":
            is_valid = False
            break

if is_valid:
    print("ok so far")
else:
    print(c, i)
