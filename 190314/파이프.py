cnt = 0
direction = "right"
def bfs(i,j,N):
    global cnt
    q = []
    q.append(i)
    q.append(j)
    q.append('right')
    while q:
        i = q.pop(0)
        j = q.pop(0)
        direction = q.pop(0)
        if i == N-1 and j == N-1:
            cnt += 1
        else:
            if direction == "right":
                di = [0,1]
                dj = [1,1]
                for k in range(2):
                    si = i + di[k]
                    sj = j + dj[k]
                    if si >= 0 and si < N and sj >= 0 and sj < N:
                        if k == 1 and i+1 < N and j+1 < N and num_list[si][sj] == 0 and num_list[i][j+1] == 0 and num_list[i+1][j]==0:
                            q.append(si)
                            q.append(sj)
                            q.append('cross')
                        elif k == 0 and num_list[si][sj] == 0:
                            q.append(si)
                            q.append(sj)
                            q.append('right')
            elif direction == "cross":
                di = [0,1,1]
                dj = [1,1,0]
                for k in range(3):
                    si = i + di[k]
                    sj = j + dj[k]
                    if si >= 0 and si < N and sj >= 0 and sj < N:
                        if k==0 and num_list[si][sj] == 0:
                            q.append(si)
                            q.append(sj)
                            q.append('right')
                        elif k == 1 and i+1 < N and j+1 < N and num_list[si][sj] == 0 and num_list[i][j+1] == 0 and num_list[i+1][j]==0:
                            q.append(si)
                            q.append(sj)
                            q.append('cross')
                        elif k == 2 and num_list[si][sj]==0:
                            q.append(si)
                            q.append(sj)
                            q.append('down')
            elif direction=="down":
                di = [1,1]
                dj = [0,1]
                for k in range(2):
                    si = i + di[k]
                    sj = j + dj[k]
                    if si >= 0 and si < N and sj >= 0 and sj < N:
                        if k == 1 and i+1 < N and j+1 < N and num_list[si][sj] == 0 and num_list[i][j+1] == 0 and num_list[i+1][j]==0:
                            q.append(si)
                            q.append(sj)
                            q.append('cross')
                        elif k == 0 and num_list[si][sj] == 0:
                            q.append(si)
                            q.append(sj)
                            q.append('down')
    return




N = int(input())
num_list = [list(map(int, input().split())) for i in range(N)]
bfs(0,1,N)
print(cnt)