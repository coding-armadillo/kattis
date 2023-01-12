h, w, n = [int(d) for d in input().split()]
b = [int(d) for d in input().split()]

i, tw, th, done = 0, 0, 0, False
while i < n:
    if tw + b[i] <= w:
        tw += b[i]
        if tw == w:
            tw = 0
            th += 1
        if th == h and tw == 0:
            done = True
            break
    else:
        break
    i += 1

print("YES" if done else "NO")
