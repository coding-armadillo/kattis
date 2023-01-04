a, b = input(), input()

a = a[::-1]
b = b[::-1]
i = 0
ans = ""
carry = 0
while i < len(a) or i < len(b):
    if i < len(a) and i < len(b):
        s = int(a[i]) + int(b[i]) + carry

    elif i < len(a):
        s = int(a[i]) + carry

    else:
        s = int(b[i]) + carry
    ans += str(s % 10)
    carry = s // 10
    i += 1
if carry:
    ans += str(carry)
print(ans[::-1])

# or simply
# print(int(a) + int(b))
