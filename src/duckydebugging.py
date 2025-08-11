while True:
    s = input()
    if s == "I quacked the code!":
        break
    elif s.endswith("?"):
        print("Quack!")
    elif s.endswith("."):
        print("*Nod*")
