from itertools import combinations

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    xtotal = sum(x)
    ytotal = sum(y)
    t = []
    for i in range(N):
        t.append(i)
    idx = list(combinations(t,N//2))
    # print(idx)
    result = []
    mV = 10000000000000000000000
    for i in range(len(idx)):
        xsum = 0
        ysum = 0
        for k in range(N//2):
            xsum += x[idx[i][k]]
            ysum += y[idx[i][k]]
        res = (xsum - (xtotal-xsum)) ** 2 + (ysum - (ytotal-ysum)) **2
        if res < mV:
            mV = res
    print('#{} {}'.format(tc, mV))
