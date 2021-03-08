t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k % 2 == 1:
        m = max(a)
        a = [m -x for x in a]
        print(*a, sep=' ')
    elif k % 2 == 0:
        m = max(a)
        a = [m -x for x in a]
        m = max(a)
        a = [m-x for x in a]
        print(*a, sep=' ')
