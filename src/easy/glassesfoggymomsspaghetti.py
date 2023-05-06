import math
d, x, y, h = input().split()
d = int(d)
x = int(x)
y = int(y)
h = int(h)
angle1 = (math.atan(y/x))-(math.atan((y-h/2)/x))
angle2 = (math.atan((y+h/2)/x))- (math.atan(y/x))

d1 = math.tan(angle1)*d
d2 = math.tan(angle2)*d

print(d1+d2)


