numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))

is_good_job = True
for i in range(1, max(numbers) + 1):
    if i not in numbers:
        is_good_job = False
        print(i)

if is_good_job:
    print("good job")
