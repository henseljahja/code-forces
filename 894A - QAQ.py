t = list(input())
c = 0
for i in range(len(t)):
    for j in range(i+1,len(t)):
        for k in range(j+1,len(t)):
            if t[i] == 'Q' and t[j] == 'A' and t[k] == 'Q':
                c+=1
            else:
                pass
print(c)
