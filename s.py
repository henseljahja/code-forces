t = int(input())
for i in range(t):
    n = int(input())
    x,y = 0,0
    c=0
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if a[i] == 1:
            x = i
            break
    for j in range(len(a)):
        if a[-j] == 1:
            y = j
            break
    c += a[x:-y].count(0)
    print(c)
