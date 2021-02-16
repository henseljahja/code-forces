n = int(input())
arr = list(map(int, input().split()))
prog, maths, pe = 0, 0, 0
prog_index, maths_index, pe_index = [], [], []
for i, x in enumerate(arr):
    if x == 1:
        prog +=1
        prog_index.append(i)
    elif x ==2:
        maths +=1
        maths_index.append(i)
    elif x ==3:
        pe+=1
        pe_index.append(i)
count=0
for i in range(min(prog,maths,pe)):
    # prog,maths,pe = prog-1, maths-1, pe-1
    if prog<1 or maths<1 or pe<1:
        break
    prog,maths,pe = prog-1, maths-1, pe-1
    count+=1
print(count)
for i in range(count):
    print(prog_index[i]+1,maths_index[i]+1,pe_index[i]+1)