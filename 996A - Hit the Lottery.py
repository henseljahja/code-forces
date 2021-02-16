x = int(input())
count = 0
arr = [100, 20, 10, 5, 1]
for i in range(len(arr)):
    count += int(x/arr[i])
    x = x % arr[i]
    # count += int(x/arr[i])
    # print(count)
print(count)