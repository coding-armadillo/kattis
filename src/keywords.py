keywords = set()
for _ in range(int(input())):
    keywords.add(input().lower().replace("-", " "))
print(len(keywords))
