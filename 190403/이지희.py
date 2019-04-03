import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = []
    for i in range(N):
        k = list(map(int,input().split()))
        for j in range(N):
            room.append([i,j,k[j]])
    cnt, result, max_result, max_cnt = 0,0,0,0

    room.sort(key=lambda x:x[2])
    for i in range(N**2):
        if i != N**2-1 and (abs(room[i+1][1]-room[i][1])+abs(room[i+1][0]-room[i][0])) == 1:
            cnt += 1
            if cnt == 1:
                result = room[i][2]
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                max_result = result
            cnt = 0
    print('#{} {} {}'.format(tc,max_result,max_cnt+1))