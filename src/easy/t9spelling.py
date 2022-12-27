n = int(input())
mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "0": " ",
}

for i in range(n):
    ans = []
    prev = ""
    for c in input():
        for d, r in mapping.items():
            if c in r:
                if d == prev:
                    ans.append(" ")
                ans.append(d * (r.index(c) + 1))
                prev = d
                break
    print(f"Case #{i+1}: {''.join(ans)}")
