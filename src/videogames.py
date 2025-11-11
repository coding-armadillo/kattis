n = int(input())
m = {
    "fishing": "alice",
    "golf": "bob",
    "hockey": "charlie",
}
for _ in range(n):
    a, _, _, _, b = input().split()
    c = m[b]
    if a == c:
        print(f"{a} already has {b}")
    else:
        print(f"{a} borrows {b} from {c}")
        m[b] = a
