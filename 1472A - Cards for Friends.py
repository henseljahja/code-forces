t = int(input())
for i in range(t):
    w,h,n = list(map(int, input().split()))
    sheet=1
    while w%2 ==0:
        w/=2
        sheet*=2
    while h%2 ==0:
        h/=2
        sheet*=2
    if sheet >= n:
        print("YES")
    else:
        print("NO")
