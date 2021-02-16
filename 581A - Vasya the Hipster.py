a,b = list(map(int, input().split()))
pair=0
single=0
while a != 0 and b != 0:
    a -= 1
    b -= 1
    pair+=1
for i in range(max(a,b)):
    if a > 1:
        a -= 2
        single+=1
    elif b > 1:
        b -= 2
        single+=1
print(pair, single)