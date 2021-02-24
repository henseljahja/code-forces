n = int(input())
t = list(input())
c = 0
for i in range(n-2):
    if t[i] == 'x' and t[i+1] == 'x' and t[i+2] == 'x':
        c+=1
print(c)





