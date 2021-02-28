t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = min(a)
    c = 0
    for i in a:
        if i != m:
            c+=1
    print(c)
