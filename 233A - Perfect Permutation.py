t = int(input())
if t % 2 == 1:
    print(-1)
else:
    x = [num for num in range(1,t+1)]
    i = 0
    while i < t:
        print(x[i+1],x[i],end=' ')
        i+=2

