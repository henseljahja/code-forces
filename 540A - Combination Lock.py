t = int(input())
x = [int(i) for i in input()]
y = [int(i) for i in input()]
arr = []
for i in range(t):
    dis = min(abs(x[i]-y[i]), 10-abs(x[i]-y[i]))
    arr.append(dis)
print(sum(arr))