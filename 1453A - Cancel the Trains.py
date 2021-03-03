for i in range(int(input())):
    n,m = map(int, input().split())
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    x,y,c = 0,0,0
    if len(n) >= len(m):
        x = n
        y = m
    else:
        x = m
        y = n
    res = [ num for num in y if(num in x)]
    print(len(res))
