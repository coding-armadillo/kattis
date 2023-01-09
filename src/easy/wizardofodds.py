import math

n, k = [int(d) for d in input().split()]
ans = math.log(n, 2) <= k
if ans:
    print("Your wish is granted!")
else:
    print("You will become a flying monkey!")
