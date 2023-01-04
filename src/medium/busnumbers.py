n = int(input())
numbers = sorted([int(d) for d in input().split()])

prev = numbers[0]
ans = {prev: 1}
for i in range(1, n):
    if numbers[i] == prev + ans[prev]:
        ans[prev] += 1
    else:
        prev = numbers[i]
        ans[prev] = 1

print(
    " ".join(
        [
            f"{key}-{key+value-1}"
            if value > 2
            else " ".join([str(d) for d in range(key, key + value)])
            for key, value in ans.items()
        ]
    )
)
