n = int(input())
times = []
for _ in range(n):
    times.append(int(input()))
if n % 2:
    print("still running")
else:
    seconds = 0
    for i in range(0, n, 2):
        seconds += times[i + 1] - times[i]
    print(seconds)
