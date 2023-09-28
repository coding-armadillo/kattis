n = int(input())
a, b = input(), input()
if n % 2:
    print(
        "Deletion", "failed" if not all([i != j for i, j in zip(a, b)]) else "succeeded"
    )
else:
    print(
        "Deletion", "failed" if not all([i == j for i, j in zip(a, b)]) else "succeeded"
    )
