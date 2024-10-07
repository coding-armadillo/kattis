n = int(input())
threes = n // 3
remainder = n % 3
if remainder == 1:
    twos = 2
    threes -= 1
elif remainder == 2:
    twos = 1
else:
    twos = 0
print(threes + twos)
print(*(threes * ["3"] + twos * ["2"]))
