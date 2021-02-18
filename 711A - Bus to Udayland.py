n = int(input())
arr = []
for i in range(n):
    x = input()
    arr.append(x)
for i in range(len(arr)):
    p = list(map(str, arr[i]))
    for j in range(len(p)-1):
        if p[j+1] == 'O' and p[j] == 'O':
            p[j+1] = '+'
            p[j] = '+'
            arr[i] = str("".join(p))
            print("YES")
            for k in arr:
                print(k)
            quit()
print("NO")