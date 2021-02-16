x = int(input())
for i in range(x):
    a,b = [int(x) for x in input().split()]
    count = 0
    if a>b:
        while a>0:
            count+=1
            a = a-b
        print(count-1)
    elif b>a:
        while b>0:
            count+=1
            b = b-a
        print(count-1)