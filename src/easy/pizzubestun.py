n = int(input())
prices = [int(input().split()[-1]) for _ in range(n)]
if n % 2:
    prices.append(0)
prices = sorted(prices, reverse=True)
print(sum(prices[i] for i in range(0, len(prices), 2)))
