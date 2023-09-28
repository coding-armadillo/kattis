n, m = [int(d) for d in input().split()]

diff = n - m
if diff > 0:
    print(f"Dr. Chaz needs {diff} more piece{'s' if diff >1 else ''} of chicken!")
else:
    diff = abs(diff)
    print(
        f"Dr. Chaz will have {diff} piece{'s' if diff >1 else ''} of chicken left over!"
    )
