n = int(input())
s = input()
stack = []
is_valid = True
for i in range(n):
    c = s[i]
    if c in ("(", "[", "{"):
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

print("Valid" if is_valid and not len(stack) else "Invalid")
