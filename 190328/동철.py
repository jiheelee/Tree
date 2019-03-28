def dong(n,N,mul):
    global maxV
    if n == N:
        if maxV < mul:
            maxV = mul
    elif mul <= maxV:
        return
    else:
        for i in range(N):
            if u[i] == 0:
                u[i] = 1
                dong(n+1,N,mul*p[n][i]*0.01)
                u[i] = 0
import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    p = [list(map(int,input().split())) for i in range(N)]
    u = [0] * N
    maxV = 0
    dong(0,N,1)
    print('#{} {}'.format(tc,format(maxV * 100, ".6f")))
