sun_years_ago, sun_cycle = [int(v) for v in input().split()]
moon_years_ago, moon_cycle = [int(v) for v in input().split()]

for t in range(1, 5001):
    if (t + sun_years_ago) % sun_cycle == 0 and (t + moon_years_ago) % moon_cycle == 0:
        print(t)
        break
