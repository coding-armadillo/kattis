k=int(input())
n=int(input())
x=[int(input()) for _ in range(n)]
print(int(sum([k**d for d in x])))