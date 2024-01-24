import sys
    

arr = []
c = [1,1]
n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    arr.append(m)
t = max(arr)
for i in range(2,t):
    c.append(c[i-2] + c[i-1])

for i in arr:
    if i == 0:
        print("1 0")
    elif i == 1:
        print("0 1")
    else:
        print(c[i-2],c[i-1])