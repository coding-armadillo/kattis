ans = []
for c in input():
    if c != "<":
        ans.append(c)
    else:
        ans.pop()
print("".join(ans))
