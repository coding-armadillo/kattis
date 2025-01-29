a, b, c = int(input()), int(input()), int(input())
m = max([a, b, c])
if m > 90:
    print("Trubbig Triangel")
elif m < 90:
    print("Spetsig Triangel")
else:
    print("Ratvinklig Triangel")
