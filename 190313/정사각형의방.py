import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):

    def dfs(i,j):
        global N
        global cnt

        di = [0,-1,0,1]
        dj = [1,0,-1,0]
        for k in range(4):
            si = i + di[k]
            sj = j + dj[k]
            if si>=0 and si<N and sj>=0 and sj<N:
                if room[si][sj] == room[i][j] + 1:
                    cnt += 1
                    dfs(si,sj)
        return cnt



    N = int(input())
    room = [list(map(int,input().split())) for i in range(N)]
    num = []
    result = []
    for i in range(N):
        for j in range(N):
            cnt = 1
            num.append(room[i][j])
            result.append(dfs(i,j))

    max_val = 0
    min_num = N ** 2

    for r in range(len(result)):
        if result[r] >= max_val:
            max_val = result[r]
    for i in range(len(num)):
        if result[i] == max_val and min_num > num[i]:
            min_num = num[i]
    print('#{} {} {}'.format(tc,min_num,max_val))