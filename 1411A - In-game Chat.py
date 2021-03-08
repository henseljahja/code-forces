t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    s = s[::-1]
    c=0
    for i in s:
        if i == ')':
            c+=1
        else:
            break
    if c > (len(s)-c):
        print("Yes")
    else:
        print("No")
