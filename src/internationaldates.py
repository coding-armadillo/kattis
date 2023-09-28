aa, bb, _ = [int(d) for d in input().split("/")]

if aa > 12 and bb <= 12:
    print("EU")
elif aa <= 12 and bb > 12:
    print("US")
else:
    print("either")
