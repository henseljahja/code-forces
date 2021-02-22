n = int(input())
c = 1
a = list(map(int, input().split()))
m = 1
for i in range(1,len(a)):
    if  a[i] > a[i-1]:
        c+=1
    else:
        if c > m:
            m = c
        c=1
    if c > m:
        m =c
print(m)
