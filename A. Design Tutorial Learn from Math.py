x = int(input())
for i in range(x):
    a,b = [int(x) for x in input().split()]
    count = 0
    while b>0:
        count+=1
        b-a
    print(count)