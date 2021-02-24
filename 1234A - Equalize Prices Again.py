q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    x = int((sum(a)+n-1)/n)
    print(x)
