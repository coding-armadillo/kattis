def f(numbers):
    prev = numbers[0]
    ans = {prev: 1}
    for i in range(1, len(numbers)):
        if numbers[i] == prev + ans[prev]:
            ans[prev] += 1
        else:
            prev = numbers[i]
            ans[prev] = 1

    parts = [
        f"{key}-{key+value-1}"
        if value > 1
        else " ".join([str(d) for d in range(key, key + value)])
        for key, value in ans.items()
    ]

    return ", ".join(parts[:-1]) + " and " + parts[-1]


c, n = [int(d) for d in input().split()]
errors = [int(d) for d in input().split()]
correct = [i for i in range(1, 1 + c) if i not in errors]

print("Errors:", f(errors))
print("Correct:", f(correct))
