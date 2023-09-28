import string

for _ in range(int(input())):
    p = set([c for c in input().lower() if c.isalpha()])
    if len(p) == 26:
        print("pangram")
    else:
        print(
            f"missing {''.join([c for c in string.ascii_lowercase[:26] if c not in p])}"
        )
