t = int(input())
for i in range(t):
    a,b,c = list(map(int, input().split()))
    x,y,z = 0,0,0
    if c%2 == 0:
        steps = int(c/2)
        tot = (a*(steps) - b*steps)
    elif c%2 == 1:
        steps = int(c/2)
        tot = (a*(steps+1) - b*steps)
    print(tot)

