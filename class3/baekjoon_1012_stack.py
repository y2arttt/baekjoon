import sys
from collections import deque

an = []
n = int(sys.stdin.readline())
dfs = deque()
for i in range(n):
    x, y, m = map(int,sys.stdin.readline().split())
    arr = []
    c = 0
    for j in range(x):
        arr.append([])
        for _ in range(y):
           arr[j].append(0)
    for _ in range(m):
        nx, ny = map(int,sys.stdin.readline().split())
        arr[nx][ny] = 1
    for ii in range(x):
        for j in range(y):
            if(arr[ii][j] == 1):
                dfs.append([ii,j])
                while True:
                    nx,ny = dfs.pop()
                    if arr[nx][ny] == 1:
                        arr[nx][ny] = 0
                        if nx - 1 >= 0:
                             dfs.append([nx-1,ny])
                        if ny - 1 >= 0:
                            dfs.append([nx,ny-1])
                        if nx + 1 < x:
                            dfs.append([nx+1,ny])
                        if ny + 1 < y:
                            dfs.append([nx,ny+1])
                    if len(dfs) == 0:
                        break
                c+= 1
                        
                    
    an.append(c)
for i in an:
    print(i)
