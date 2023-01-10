s = input()
s = [ord(c) for c in s]
s = sum(s) // len(s)
print(chr(s))
