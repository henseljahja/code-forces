n = int(input())
arr = []
mishka, chris = 0,0
for i in range(n):
    a,b = list(map(int, input().split()))
    if a>b:
        mishka +=1
    elif a<b:
        chris +=1
    else:
        pass
if mishka > chris:
    print("Mishka")
elif mishka < chris:
    print("Chris")
else:
    print("Friendship is magic!^^")