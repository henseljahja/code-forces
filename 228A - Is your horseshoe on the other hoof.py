x = sorted(list(map(int,input().split())))
count=0
for i in range(len(x)-1):
    if x[i]==x[i+1]:
        count+=1
print(count)
# print(len(x))