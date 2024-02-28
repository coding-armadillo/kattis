n = input()
k = 0
while n:
    k += 1
    if n.startswith(str(k)):
        n = n[len(str(k)) :]
    else:
        k = -1
        break
print(k)
