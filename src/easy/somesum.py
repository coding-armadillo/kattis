n = int(input())
if n == 1:
    print("Either")
elif n == 2:
    print("Odd")
elif n % 2 == 0:
    print("Even" if (n / 2) % 2 == 0 else "Odd")
else:
    print("Either")
