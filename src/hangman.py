word = set(list(input()))
guess = input()
tries = 0
correct = 0
for c in guess:
    if c in word:
        correct += 1
    else:
        tries += 1

    if correct == len(word):
        break

if tries >= 10:
    print("LOSE")
else:
    print("WIN")
