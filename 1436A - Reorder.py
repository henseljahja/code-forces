t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    c = list(map(int, input().split()))
    print("YES" if sum(c) == b else "NO")
