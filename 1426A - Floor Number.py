t = int(input())
for i in range(t):
    n, x = map(int,input().split())
    floor = 1
    for i in range(max(n,x)):
        p = (i*x+3)
        q = ((i+1)*x+2)
        if n <= 2:
            print(floor)
            break
        elif p <= n <= q:
            floor+=1
            print(floor)
            break
        else:
            floor+=1
            continue

