n = int(input())
ar = list(map(int, input().split()))
ar_max = max(ar)
count = 0
for i in ar:
    if i < ar_max:
        count += ar_max - i
    else:
        pass
print(count)