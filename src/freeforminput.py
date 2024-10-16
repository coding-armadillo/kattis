while True:
    try:
        s = input()
        print(sum(float(n) for n in s.replace(" ", "").split(",")))
    except:
        break
