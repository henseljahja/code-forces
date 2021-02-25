t = int(input())
for i in range(t):
    a,b = list(map(int, input().split()))
    print("YES" if a%b == 0 else "NO") 
