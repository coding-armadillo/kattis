R, C = [int(v) for v in input().split()]

chocolate_bar_cuts = (R * C)-1

if chocolate_bar_cuts % 2 == 1:
    print("Alf")
else:
    print("Beata")
