for _ in range(int(input())):
    b, p = [float(d) for d in input().split()]
    min_abpm = 60 / p * (b - 1)
    bpm = 60 * b / p
    max_abpm = 60 / p * (b + 1)
    print(f"{min_abpm:.4f} {bpm:.4f} {max_abpm:.4f}")
