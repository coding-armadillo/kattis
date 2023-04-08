message = input()

l = []
l.append(message[0])
for i in message[1: ]:
    if i != l[-1]:  
        l.append(i)
print("".join(l))