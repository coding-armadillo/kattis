input()
h, m = [int(d) for d in input().split(":")]
is_weekend = input() in ["sat", "sun"]
bad_weather = int(input())
snow = int(input())
holiday = int(input())
m = 60 * h + m
if is_weekend:
    m *= 2
if bad_weather:
    m *= 2
if snow:
    m *= 3
if holiday:
    m *= 3
h = m // 60
m = m % 60
print(f"{h}:{str(m).zfill(2)}")
