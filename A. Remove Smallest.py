a = int(input())
answer = []
for i in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    x = list(set(c))
    count=0
    
    for i in range(len(x)):
        if c.count(x[i]) == 2:
            count+=1
    if len(x) > 2:
        answer.append("NO")
    else:
        if count == 1 or count == 0:
            answer.append("YES")
        else:
            answer.append("NO")
for i in range(len(answer)):
    print(answer[i])