def dij(s, v):
    u = [s]
    for i in range(1, v+1):
        d[i] = adj[s][i]

    while len(u) != v:
        minV = 100
        w = 0
        for i in range(1,v+1):
            if i not in u:
                if d[i]<minV:
                    minV = d[i]
                    w = i
        u.append(w)
        print(u)
        for i in range(v+1):
            if w!=i and adj[w][i] != 100:
                d[i] = min(d[i],d[w]+adj[w][i])
        print(d)


T = int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split())
    adj = [[100] * (N+1) for i in range(N+1)]
    for i in range(N+1):
        adj[i][i] = 0
    for i in range(E):
        s, e, w = map(int,input().split())
        adj[s][e] = w
    d = [0] * (N + 1)

    for i in range(N+1):
        print(adj[i])
    dij(0,N)
    print('#{} {}'.format(tc,d[N]))







