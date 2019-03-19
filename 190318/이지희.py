def ramp(n,i,N,r,t):
    if i == N-1:
        return 1
    if n[i] == n[i+1]:
        # print(n[i])
        return ramp(n,i+1,N,r,t+1)
    else:
        if abs(n[i]-n[i+1]) > 1:
            return 0
        if n[i+1] > n[i]:
            if t < r:
                return 0
            else:
                return ramp(n,i+1, N, r, 1)
        else:
            k = 0
            i += 1
            while i+k <= N-1 and n[i+k]==n[i]:
                k += 1
            if k < r:
                return 0
            else:
                return ramp(n,i+k-1,N,r,k-r)

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, r = map(int,input().split())
    num = [list(map(int,input().split())) for i in range(N)]
    cnt = 0
    for i in range(N):
        c = []
        for j in range(N):
            c.append(num[j][i])
        num.append(c)
    for n in num:
        cnt += ramp(n,0,N,r,1)
    print(cnt)

