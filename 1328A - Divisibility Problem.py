t = int(input())
for i in range(t):
    a,b = [int(x) for x in input().split()]
    if a % b == 0:
        print(0)
    elif a<b :
        print(b-a)
    else:
        print(b-(a%b)) 