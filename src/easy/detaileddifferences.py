for _ in range(int(input())):
    s1, s2 = input(), input()
    result = ["." if c1 == c2 else "*" for c1, c2 in zip(s1, s2)]
    print(s1)
    print(s2)
    print("".join(result))
