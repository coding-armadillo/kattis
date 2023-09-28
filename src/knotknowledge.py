input()
total = set(input().split())
known = set(input().split())
print((total - known).pop())
