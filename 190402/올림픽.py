T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    count = [0] * N
    for b in B:
        for n in range(N):
            if A[n] <= b:
                count[n] += 1
                break
    mi = 0
    for i in range(N):
        if count[i]> count[mi]:
            mi = i
    print('#{} {}'.format(tc,mi+1))

