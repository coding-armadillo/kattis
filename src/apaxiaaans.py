name = input()
compact = ""
for s in name:
    if not compact or s != compact[-1]:
        compact += s
print(compact)
