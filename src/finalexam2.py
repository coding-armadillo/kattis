n = int(input())
ans, score = [], 0
for i in range(n):
    ans.append(input())
    if i == 0:
        continue
    if ans[i] == ans[i - 1]:
        score += 1
print(score)
