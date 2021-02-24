x = list(input())
p = len(x)
i=0
while i < p:
#for i in range(p-1):
    if x[i] =='-': 
        if x[i+1] == '.':
            print('1',end='')
        elif x[i+1] == '-':
            print('2',end='')
        i+=2
    else:
        print('0',end='')
        i+=1
