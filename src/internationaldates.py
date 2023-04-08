AA, BB, CCCC = [int(d) for d in input().split("/")]

if AA > 12 and BB<=12:
    print("EU")
elif AA <= 12 and BB >12:
    print("US")
elif AA<=12 and BB <=12:
    print("either")
