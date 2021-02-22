# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     if a[0] + a[1] > a[-1]:
#         print(-1)
#     else:
#         print(1, 2, n)

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
