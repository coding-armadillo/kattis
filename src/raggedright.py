l = []
while True:
    try:
        s = input()
    except:
        break
    l.append(len(s))
m = max(l)
print(sum([(n - m) ** 2 for n in l[:-1]]))
