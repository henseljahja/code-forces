n = int(input())
a = list(map(int, input().split()))
a = a[::-1]
a = sorted(set(a), key = a.index)
print(len(a))
print(*a[::-1])
