ans = []
for i in range(5):
    row = input()
    if "FBI" in row:
        ans.append(str(i + 1))
if not ans:
    print("HE GOT AWAY!")
else:
    print(" ".join(ans))
