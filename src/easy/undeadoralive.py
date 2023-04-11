s = input()

smiley = ":)" in s

frowny = ":(" in s

if not frowny and smiley:
    print("alive")

elif frowny and not smiley:
    print("undead")

elif frowny and smiley:
    print("double agent")

else:
    print("machine")
