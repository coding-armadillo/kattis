a, b = input(), input()
da, ta = a.split()
db, tb = b.split()
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
da = weekdays.index(da)
db = weekdays.index(db)
ha, ma = [int(d) for d in ta.split(":")]
hb, mb = [int(d) for d in tb.split(":")]

mins, hours, days = mb - ma, hb - ha, db - da
if mins < 0:
    mins += 60
    hours -= 1
if hours < 0:
    hours += 24
    days -= 1
if days < 0:
    days += 7

parts = [
    f'{a} {b}{"s" if a>1 else ""}'
    for a, b in zip([days, hours, mins], ["day", "hour", "minute"])
    if a > 0
]
size = len(parts)
if size == 1:
    print(parts[0])
elif size == 2:
    print(" and ".join(parts))
elif size == 3:
    print(", ".join(parts))
else:
    print("7 days")
