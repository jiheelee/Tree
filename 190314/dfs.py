cnt = 0
direction = "right"


def dfs(i, j, N, direction):
    global cnt


    if i == N - 1 and j == N - 1:
        cnt += 1
        return
    else:
        if direction == "right":
            di = [0, 1]
            dj = [1, 1]
            for k in range(2):
                si = i + di[k]
                sj = j + dj[k]
                if si >= 0 and si < N and sj >= 0 and sj < N:
                    if k == 1 and i + 1 < N and j + 1 < N and num_list[si][sj] == 0 and num_list[i][j + 1] == 0 and \
                            num_list[i + 1][j] == 0:
                        dfs(si, sj, N, "cross")
                    elif k == 0 and num_list[si][sj] == 0:
                        dfs(si, sj, N, "right")
        elif direction == "cross":
            di = [0, 1, 1]
            dj = [1, 1, 0]
            for k in range(3):
                si = i + di[k]
                sj = j + dj[k]
                if si >= 0 and si < N and sj >= 0 and sj < N:
                    if k == 0 and num_list[si][sj] == 0:
                        dfs(si, sj, N, "right")
                    elif k == 1 and i + 1 < N and j + 1 < N and num_list[si][sj] == 0 and num_list[i][
                        j + 1] == 0 and num_list[i + 1][j] == 0:
                        dfs(si, sj, N, "cross")
                    elif k == 2 and num_list[si][sj] == 0:
                        dfs(si, sj, N, "down")
        elif direction=="down":
            di = [1, 1]
            dj = [0, 1]
            for k in range(2):
                si = i + di[k]
                sj = j + dj[k]
                if si >= 0 and si < N and sj >= 0 and sj < N:
                    if k == 1 and i + 1 < N and j + 1 < N and num_list[si][sj] == 0 and num_list[i][j + 1] == 0 and \
                            num_list[i + 1][j] == 0:
                        dfs(si, sj, N, "cross")
                    elif k == 0 and num_list[si][sj] == 0:
                        dfs(si, sj, N, "down")
    return


N = int(input())
num_list = [list(map(int, input().split())) for i in range(N)]
dfs(0, 1, N, "right")
print(cnt)