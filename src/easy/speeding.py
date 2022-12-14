n = int(input())
mile, time, max_speed = 0, 0, 0
for _ in range(n):
    t, s = [int(d) for d in input().split()]
    if not t and not s:
        continue
    speed = int((s - mile) / (t - time))
    if speed > max_speed:
        max_speed = speed
    mile, time = s, t
print(max_speed)
