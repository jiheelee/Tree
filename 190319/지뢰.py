def bfs(i,j,N):
    global cnt
    cnt += 1
    di = [0,-1,0,1,1,-1,-1,1]
    dj = [1,0,-1,0,1,1,-1,-1]
    q = []
    check = 0
    for k in range(8):
        si = i + di[k]
        sj = j + dj[k]

        if si>=0 and si<N and sj>=0 and sj<N:
            q.append((si, sj))
            if room[si][sj] == "*":
                check = 1
    if check == 0:

        room[i][j] = 0
        while q:
            a = q.pop(0)
            sum = 0
            for k in range(8):
                ti = a[0] + di[k]
                tj = a[1] + dj[k]
                if ti >= 0 and ti < N and tj >= 0 and tj < N:
                    if room[ti][tj] == "*":
                        sum += 1
            room[a[0]][a[1]] = sum

    return



# import sys
# sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(input()) for i in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if room[i][j] == ".":
                bfs(i,j,N)
                print(room)
    print(cnt)
