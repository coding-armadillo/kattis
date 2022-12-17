_ = input()
at_bats = [int(d) for d in input().split()]
ans = [d for d in at_bats if d >= 0]
print(sum(ans) / len(ans))
