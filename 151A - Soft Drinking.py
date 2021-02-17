n, k, l, c, d, p, nl, np = list(map(int, input().split()))
x = k*l
y = x/nl
z = c*d
q = p/np
ans = min(y,z,q)/n
print(int(ans))