from string import ascii_lowercase

s = [c for c in input().lower() if c in ascii_lowercase]

f = False
if len(s) == 1:
    f = True

if not f:
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            f = True
            break

if not f:
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            f = True
            break

print("Palindrome" if f else "Anti-palindrome")
