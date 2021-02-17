n = int(input())
arr = list(map(int, input().split()))
sereja, dima = 0,0 
for i in range(1,n+1):
    # maxes = max(arr)
    # if i % 2 == 1:
    #     sereja += maxes
    # elif i % 2 == 0:
    #     dima += maxes
    maxes_count = arr.count(max(arr))
    maxes = max(arr)
    if maxes_count == 1:
        # arr.remove(max(arr))
        # maxes = max(arr)
        if i % 2 == 1:
            sereja += maxes
        elif i % 2 == 0:
            dima += maxes
        # else :
        #     break
    elif maxes_count > 1:
        for i in range(maxes_count):
            # maxes = max(arr)
            if i % 2 == 1:
                sereja += maxes
            elif i % 2 == 0:
                dima += maxes
            # else :
            #     break
    arr.remove(max(arr))
    # print(maxes_count)
print(sereja, dima)