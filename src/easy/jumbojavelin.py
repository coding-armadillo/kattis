n = int(input())
length = 0
for _ in range(n):
    length += int(input())
length -= n - 1
print(length)
