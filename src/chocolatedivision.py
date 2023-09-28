r, c = [int(v) for v in input().split()]

chocolate_bar_cuts = (r * c) - 1

if chocolate_bar_cuts % 2 == 1:
    print("Alf")
else:
    print("Beata")
