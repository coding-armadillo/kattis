sun_years_ago, sun_back = [int(v) for v in input().split()]
moon_years_ago, moon_back = [int(v) for v in input().split()]

for t in range(5001):
    if (t + sun_years_ago) % sun_back == 0 and (t + moon_years_ago) % moon_back == 0:
        print(t)
        break

    




