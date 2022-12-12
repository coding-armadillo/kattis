n = int(input())
for _ in range(n):
    numbers = [int(d) for d in input().split()[1:]]
    ave = sum(numbers) / len(numbers)
    above_ave = [d > ave for d in numbers]
    print(f"{sum(above_ave)/len(numbers):.3%}")
