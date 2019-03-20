def way(i,j,N,K,t,cnt):
    global max_val
    di = [0,-1,0,1]
    dj = [1,0,-1,0]
    for k in range(4):
        si = i + di[k]
        sj = j + dj[k]
        if si>=0 and sj >=0 and si<N and sj<N:
            if mountain[si][sj] < mountain[i][j]:
                # print(mountain[si][sj])
                way(si,sj,N,K,t+1,cnt)
                if max_val < t+1:
                    max_val = t+1
            elif (mountain[si][sj]-mountain[i][j]+1) <= K and cnt ==1:
                # print(mountain[si][sj])
                mountain[si][sj] = mountain[si][sj] - (mountain[si][sj]-mountain[i][j]+1)
                way(si,sj,N,K,t+1,cnt-1)
                if max_val < t+1:
                    max_val = t+1



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
    # print(q)
    total_max = 0
    q = [(2,4)]
    print(q)
    while q:

        a = q.pop(0)
        max_val = 0
        way(a[0],a[1],N,K,1,1)
        print(max_val)
        if max_val > total_max:
            total_max = max_val
    print(total_max)
