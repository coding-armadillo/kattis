n = int(input())

height = 0
while True:
    height += 1
    blocks = (2 * height - 1) ** 2
    if blocks > n:
        height -= 1
        break
    n -= blocks

print(height)
