import re

input()
s = input()
if "lv" in s:
    print(0)
elif re.findall(r"(l\wv|l\w|\wv)", s):
    print(1)
else:
    print(2)
