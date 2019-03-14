T = int(input())
for tc in range(1,T+1):
    N, direction = input().split()
    N = int(N)
    num_list = [list(map(int,input().split())) for i in range(N)]
    new= [[0] * N for i in range(N)]
    final = [[0] * N for i in range(N)]
    if direction == "left":
        new = num_list
    elif direction == "down":
        for i in range(N):
            for j in range(N):
                new[i][j] = num_list[N-1-j][i]
    elif direction == "up":
        for i in range(N):
            for j in range(N):
                new[i][j] = num_list[j][N - 1 - i]
    else:
        for i in range(N):
            for j in range(N):
                new[i][j] = num_list[i][N-1-j]

    result = []
    for line in new:
        t = []
        for i in range(N):
           if line[i] != 0:
               t.append(line[i])
        stack = []
        while t:
            if len(t)>1 and t[0] == t[1]:
                a = t.pop(0)
                b = t.pop(0)
                c = a + b
                stack.append(c)
            else:
                a = t.pop(0)
                stack.append(a)
        stack.extend([0]*(N-len(stack)))
        result.append(stack)

    if direction=="up":
        for i in range(N):
            for j in range(N):
                final[i][j] = result[N-1-j][i]
    elif direction=='right':
        for i in range(N):
            for j in range(N):
                final[i][j] = result[i][N-1-j]
    elif direction=='down':
        for i in range(N):
            for j in range(N):
                final[i][j] = result[j][N - 1 - i]
    else:
        final = result
    print("#{}".format(tc))
    for i in final:
        print(" ".join(map(str,i)))

