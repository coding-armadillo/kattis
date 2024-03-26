from math import pi

d = int(input())
a = int(input())
b = int(input())
h = int(input())
m = pi * d * d / 4
t = (a + b) * h / 2
if m == t:
    print("Jafn storar!")
elif m > t:
    print("Mahjong!")
else:
    print("Trapizza!")
