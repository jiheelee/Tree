def f(n,k,s):
    global minV
    if n == k:
        if minV > s:
            minV = s
        return
    elif minV <= s:
        return
    else:
        for i in range(k):
            if u[i] == 0:
                u[i] = 1
                f(n+1,k,s+factory[n][i])
                u[i] = 0



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    factory = [list(map(int,input().split())) for i in range(N)]
    minV = 99 * N
    u = [0] * N

    f(0,N,0)

    print('#{} {}'.format(tc,minV))
