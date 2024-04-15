s1 = input()
s2 = input()
print(sum(a != b for a, b in zip(s1, s2)) + 1)
