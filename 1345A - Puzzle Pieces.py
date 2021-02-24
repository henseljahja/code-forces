t = int(input())
for i in range(t):
    a,b = list(map(int, input().split()))
    if a==1 or b==1 or a*b ==4:
        print("YES")
    else:
        print("NO")
