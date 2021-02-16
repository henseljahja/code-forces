a,b = list(map(int, input().split()))
arr = []
color = ["C", "M", "Y"]
for i in range(a):
    color = list(input().split())
    arr += color
for i in arr:
    if i == "C" or i == "M" or i == "Y":
        print("#Color")
        quit()
# if any(x in arr for x in color):
#     print("#Color")
print("#Black&White")