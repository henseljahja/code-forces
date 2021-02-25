a,b = list(map(int, input().split()))
kid = 0
for i in range(a):
    x,y = list(input().split())
    if x == '+':
        b += int(y)
    elif x == '-':
        if b >= int(y):
            b -= int(y)
        elif b < int(y):
            kid+=1
print(b,kid)
