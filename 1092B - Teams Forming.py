t = int(input())
a = list(map(int , input().split()))
a.sort()
c = 0
for i in range(0,t,2):
    x,y = a[i], a[i+1]
    c+= y-x
print(c)
