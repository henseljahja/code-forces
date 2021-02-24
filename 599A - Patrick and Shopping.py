d1, d2, d3 = list(map(int, input().split()))
route = 0
x = min(d1,d2+d3)+ min(d3, d1+d2)+min(d2,d1+d3)
print(x)

