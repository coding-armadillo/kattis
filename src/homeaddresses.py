a = []
while True:
    s = input()
    if s == "q":
        break
    a.append(s)
print(a)
print([tuple(s.split()) for s in a])
