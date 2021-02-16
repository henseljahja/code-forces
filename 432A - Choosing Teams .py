a, b = list(map(int, input().split()))
arr = list(map(int, input().split()))
team = 0
eligible = 0
for i in arr:
    if (i+b) <= 5:
        eligible +=1
print(int(eligible/3))