d = [int(input()) for _ in range(9)]
diff = sum(d) - 100
end = False
for i in range(8):
    for j in range(i + 1, 9):
        if d[i] + d[j] == diff:
            end = True
            break
    if end:
        break
print("\n".join([str(d[k]) for k in range(9) if k not in [i, j]]))
