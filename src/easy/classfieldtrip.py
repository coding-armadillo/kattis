a = input()
b = input()

i, j = 0, 0
ans = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        ans.append(a[i])
        i += 1
    else:
        ans.append(b[j])
        j += 1


ans += a[i:] if i < len(a) else b[j:]

print("".join(ans))
