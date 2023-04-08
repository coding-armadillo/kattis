a = input()

Smile = ":)" in a
        
Frown = ":(" in a

if not Frown and Smile:
    print("alive")
    
elif Frown  and not Smile:
    print("undead")

elif Frown and Smile:
    print("double agent")

else:
    print("machine")