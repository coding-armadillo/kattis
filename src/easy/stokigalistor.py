n = int(input())
a = [int(d) for d in input().split()]
s = sorted(a)
print(sum([ i!=j for i ,j in zip(a,s)]))