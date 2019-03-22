def way(i,j,N,K,t,cnt):
    global max_val
    if t  > max_val:
        max_val = t
    di = [0,-1,0,1]
    dj = [1,0,-1,0]
    visited[i][j] = 1
    for k in range(4):
        si = i + di[k]
        sj = j + dj[k]
        if si>=0 and sj >=0 and si<N and sj<N:
            if cnt > 0:
                if (mountain[i][j] - cnt) > mountain[si][sj] and visited[si][sj] == 0:
                    way(si, sj, N, K, t+1, -1)

            elif mountain[si][sj] < mountain[i][j] and visited[si][sj]==0:
                way(si,sj,N,K,t+1,cnt)

            elif visited[si][sj]==0 and (mountain[si][sj]-mountain[i][j]+1) <= K and cnt ==0:
                way(si,sj,N,K,t+1,mountain[si][sj]-mountain[i][j]+1)

    visited[i][j] = 0

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    mountain = [list(map(int,input().split())) for i in range(N)]
    max_height = 0
    q = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_height:
                max_height = mountain[i][j]
                q = []
                q.append((i,j))
            elif mountain[i][j] == max_height:
                q.append((i,j))
    max_val = 0
    print(q)
    while q:
        visited = [[0] * N for i in range(N)]
        a = q.pop(0)
        way(a[0],a[1],N,K,1,0)
        print(max_val)

    print('#{} {}'.format(tc,max_val))
