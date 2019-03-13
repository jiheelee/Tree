import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for i in range(N)]
    num_list = []
    for i in range(N):
        for j in range(N):
            num_list.append([room[i][j],i,j])

    num_list= sorted(num_list,key=lambda n:n[0])
    # print(num_list)
    min_val = N**2
    cnt = 1
    max_cnt = 0
    check = 0
    val = N**2

    for i in range(N**2):

        if (i+1)<N**2 and abs(num_list[i][1]-num_list[i+1][1]) + abs(num_list[i][2]-num_list[i+1][2]) == 1:
            if check == 0:
                val = num_list[i][0]
            cnt += 1
            check = 1
        else:
            if cnt == max_cnt and val < min_val:
                min_val = val
            elif cnt > max_cnt:
                max_cnt = cnt
                min_val = val
            cnt = 1
            check = 0
    print('#{} {} {}'.format(tc,min_val,max_cnt))