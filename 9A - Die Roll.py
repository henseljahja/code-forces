a,b = map(int, input().split())
x = max(a,b)
# s = [i for i in range(1,7)]
prob = (6-(x-1))/6
if prob == 0:
    print("0/1")
elif prob == (4/6):
    print("2/3")
elif prob == (3/6):
    print("1/2")
elif prob == (2/6):
    print("1/3")
elif prob == 1:
    print("1/1")
else:
    print(6-(x-1),"/",6, sep='')