start, end = 1, 1000
while True:
    guess = (start + end) // 2
    print(guess)
    resp = input()
    if resp == "correct":
        break
    elif resp == "higher":
        start = guess + 1
    else:
        end = guess
