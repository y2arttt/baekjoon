import sys
import math

n = int(sys.stdin.readline())
k = 0
i = 0
for _ in range(n+1):
    i += 1
    t = i
    m = int(math.log10(i)) # 자릿수 확인하기
    for j in range(0,m+1):
        t += i // (10 ** j) % 10 # 자리의 수 구하기
    if t  == n:
        print(i)
        k = 1
        break
if k < 1:
    print(0)