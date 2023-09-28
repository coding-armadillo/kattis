l = []
while True:
    try:
        l.append(input().split("|"))
    except:
        break

l = [l[i][0] for i in range(len(l))] + [" "] + [l[i][1] for i in range(len(l))]
print("".join(l))
