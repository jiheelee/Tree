import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):

    E, N = map(int,input().split())
    node = list(map(int,input().split()))
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)

    for i in range(E):
        n1 = node[i*2]
        n2 = node[i*2+1]
        if ch1[n1] == 0:
            ch1[n1] = n2
        else:
            ch2[n1] = n2
    cnt = 1
    def cal(N):
        global cnt
        if N == 0:
            return
        else:
            n1 = ch1[N]
            n2 = ch2[N]
            if n1 != 0:
                cnt += 1
                cal(n1)
            if n2 != 0:
                cnt += 1
                cal(n2)

    cal(N)
    print('#{} {}'.format(tc,cnt))