t = int(input())
x = 24*60
for i in range(t):
    h,m = list(map(int, input().split()))
    h *= 60
    ans = x - (h+m)
    print(ans)