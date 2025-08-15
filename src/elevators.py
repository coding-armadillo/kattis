z, n = input().split()
n = int(n)
if z == "residential":
    if n == 1:
        print(0)
    elif n in range(2, 6):
        print(1)
    elif n in range(6, 11):
        print(2)
    elif n in range(11, 16):
        print(3)
    elif n in range(16, 21):
        print(4)
elif z == "commercial":
    if n == 1:
        print(0)
    elif n in range(2, 8):
        print(1)
    elif n in range(8, 15):
        print(2)
    elif n in range(15, 21):
        print(3)
elif z == "industrial":
    if n == 1:
        print(0)
    elif n in range(2, 5):
        print(1)
    elif n in range(5, 9):
        print(2)
    elif n in range(9, 13):
        print(3)
    elif n in range(13, 17):
        print(4)
    elif n in range(17, 21):
        print(5)
