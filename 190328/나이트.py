def bfs(N,si,sj,ei,ej):
    visited[si][sj] = 1
    di = [1,2,2,1,-1,-2,-2,-1]
    dj = [-2,-1,1,2,2,1,-1,-2]
    q = []
    q.append(si)
    q.append(sj)
    while q:
        i = q.pop(0)
        j = q.pop(0)
        for k in range(8):
            ai = i + di[k]
            aj = j + dj[k]
            if ai>=0 and ai < N and aj>=0 and aj<N and visited[ai][aj] == 0:
                visited[ai][aj] = visited[i][j] + 1
                if ai == ei and aj == ej:
                    return visited[ai][aj] - 1
                q.append(ai)
                q.append(aj)
    return 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    si, sj = map(int,input().split())
    ei, ej = map(int,input().split())
    visited = [[0] * N for i in range(N)]

    print(bfs(N,si,sj,ei,ej))


