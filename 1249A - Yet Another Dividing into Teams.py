q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c= False
    for i in range(len(a)-1):
        if a[i+1] - a[i] ==1:
            c = True
    if c:
        print(2)
    else: print(1)
