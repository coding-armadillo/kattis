while True:
    try:
        line = input()
    except:
        break
    a, b = [int(d) for d in line.split()]
    print(abs(a - b))
