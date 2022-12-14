from datetime import datetime

d, m = [int(d) for d in input().split()]
print(datetime(year=2009, month=m, day=d).strftime("%A"))
