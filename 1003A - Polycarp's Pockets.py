t = int(input())
s = list(map(int, input().split()))
x = max(set(s), key=s.count)
print(s.count(x))
