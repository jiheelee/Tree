for tc in range(1,11):
    N = int(input())
    ch1 = [0] * (N +1)
    ch2 = [0] * (N +1)
    alp = [0] * (N+1)

    for i in range(N):
        num_list = list(input().split())
        alp[int(num_list[0])] = num_list[1]
        if len(num_list) >= 3:
            ch1[int(num_list[0])] = int(num_list[2])
        if len(num_list) >= 4:
            ch2[int(num_list[0])] = int(num_list[3])

    print('#{}'.format(tc),end= " ")
    def lrv(n):
        if n > 0:
            lrv(ch1[n])
            print(alp[n],end="")
            lrv(ch2[n])
    lrv(1)
    print()


