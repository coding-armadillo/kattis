n=int(input())
a = [int(d) for d in input().split()]
t =0
m = 0
for i in range(1,7):
    for j in range(1,7):
        t +=1
        if i+j in a:
            m+=1
print(m/t)
    