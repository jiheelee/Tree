import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(10)]
    res_max = []
    res_min = []

    col = []
    for i in range(10):
        col.append(sum(arr[i]))




    row = []
    for i in range(10):
        row_base = []
        for j in range(10):
            row_base.append(arr[j][i])
        row.append(sum(row_base))




    slash_base = []
    slash_reverse = []
    for i in range(10):
        for j in range(10):
            if i == j:
                slash_base.append(arr[i][j])
                slash_reverse.append(arr[i][9-i])


    res_max.append(max(col))
    res_max.append(max(row))
    res_max.append(sum(slash_base))
    res_max.append(sum(slash_reverse))

    res_min.append(min(col))
    res_min.append(min(row))
    res_min.append(sum(slash_base))
    res_min.append(sum(slash_reverse))




    final = max(res_max)-min(res_min)
    print("#{} {}".format(tc, final))





