a,b = list(map(int,input().split()))
time_needed = 240-b
problem_time = 5
count=0 
time_total = 0
for i in range(1, a+1):
    time_total += problem_time*i
    if time_total <= time_needed:
        count+=1 
print(count)