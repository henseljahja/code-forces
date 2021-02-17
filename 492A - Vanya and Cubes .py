n = int(input())
count = 0 
x = 0
for i in range(0,n+1):
    count += i
    if (n - count) >= 0:
        x +=1
        n -= count
    else :
        break
print(x-1)
    