from datetime import datetime

year = int(input())

mother = datetime(year, 5, 1).isoweekday()
father = datetime(year, 6, 1).isoweekday()

x = 7 - mother
y = 7 - father
daymother = 1 + x + 7
dayfather = 1 + y + 14

daymother = datetime(year, 5, daymother)
dayfather = datetime(year, 6, dayfather)

print(((dayfather - daymother).days) // 7, "weeks")
