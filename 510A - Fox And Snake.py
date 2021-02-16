a,b = [int(x) for x in input().split()]
for i in range(1,a+1):
    # for j in range(1,b+1):
    # print(i)
    if i % 4 == 2:
        print("."*(b-1)+"#")   
    elif i % 4 == 0:
        print("#"+"."*(b-1))
    else:
        print("#"*b)
    
        #print("#"*b)
        #print("."*(b-1)+"#")
        #print("#"+"."*(b-1))