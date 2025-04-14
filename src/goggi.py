s = input()
a, b = s.split("?")
a, b = int(a), int(b)
if a == b:
    print("Goggi svangur!")
elif a > b:
    print(">")
else:
    print("<")
