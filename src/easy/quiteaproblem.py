while True:
    try:
        line = input()
    except:
        break

    if "problem" in line.lower():
        print("yes")
    else:
        print("no")
