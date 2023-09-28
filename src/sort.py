from collections import Counter

n, c = [int(d) for d in input().split()]
num = [int(d) for d in input().split()]

freq = Counter(num)
print(
    " ".join(
        [
            str(d)
            for d in sorted(
                num, key=lambda k: (freq[k], n - num.index(k)), reverse=True
            )
        ]
    )
)
