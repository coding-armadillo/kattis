while True:
    try:
        n = [int(d) for d in input().split()]
    except:
        break

    for i in range(len(n)):
        if n[i] == sum([n[j] for j in range(len(n)) if j != i]):
            print(n[i])
            break
