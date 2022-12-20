moves = input()
ball = [1, 0, 0]
for move in moves:
    if move == "A":
        ball[0], ball[1] = ball[1], ball[0]
    if move == "B":
        ball[1], ball[2] = ball[2], ball[1]
    if move == "C":
        ball[0], ball[2] = ball[2], ball[0]

if ball[0]:
    print(1)
elif ball[1]:
    print(2)
else:
    print(3)
