import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) # N - 보드 한 변의 길이, M - 놓을 돌 수
    board = [[0] * (N+1) for i in range(N+1)] # 오셀로 판 만들기
    board[N//2][N//2], board[N//2+1][N//2+1] = 2, 2 # 가운데 돌 놓고 시작
    board[N//2][N//2+1], board[N//2+1][N//2] = 1, 1

    for m in range(M):
        x, y, stone = map(int,input().split())
        board[y][x] = stone
        dy = [0,-1,0,1,1,-1,-1,1]
        dx = [1,0,-1,0,1,1,-1,-1]
        for k in range(8):
            sy = y + dy[k]
            sx = x + dx[k]
            if sy >= 0 and sx >= 0 and sy < N+1 and sx < N+1:
                if board[sy][sx] == 0 or board[sy][sx] == stone:
                    pass
                else:
                    q = []
                    q.append((sy,sx))
                    c = 0
                    while sy+dy[k] > 0 and sx+dx[k] > 0 and sy+dy[k] < N+1 and sx+dx[k] < N+1:
                        sy += dy[k]
                        sx += dx[k]
                        if board[sy][sx] == 0:
                            break
                        if board[sy][sx] == stone:
                            c = 1
                            break
                        q.append((sy,sx))
                    if c == 1:
                        while q:
                            yx = q.pop(0)
                            board[yx[0]][yx[1]] = stone
    cnt1 = 0
    cnt2 = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if board[i][j] == 1:
                cnt1 += 1
            elif board[i][j] ==2:
                cnt2 += 1
    print("#{} {} {}".format(tc,cnt1,cnt2))
