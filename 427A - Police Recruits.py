n = int(input())
x = list(map(int, input().split()))
crime = 0
cops = 0
untreated = 0

for i in (x):
    if i < 0:
        if cops >= 1:
            cops -= 1
        elif cops == 0:
            untreated +=1
    if i > 0:
        cops += i
print(untreated)