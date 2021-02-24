a,b = list(map(int, input().split()))
c = 1
for i in range(1,min(a,b)+1):
    c *= i
print(c)
