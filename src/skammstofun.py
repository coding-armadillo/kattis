_ = input()
words = input().split()
print("".join([w[0] for w in words if w[0].isupper()]))
