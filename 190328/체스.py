def chess(N,cnt,former):
    global result
    global q
    if cnt == N:
        result += 1
        return
    else:
        for c in range(N):
            if c not in q:
                check = 0
                for i in range(cnt):
                    if abs(q[i] - c) == (cnt - i):
                        check = 1
                if check == 0:
                    q.append(c)
                    chess(N,cnt+1,c)
                    q.pop(-1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    q = []
    result = 0
    chess(N, 0, -2)
    print('#{} {}'.format(tc,result))