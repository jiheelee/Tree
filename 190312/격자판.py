T = int(input())
num_list = [list(map(int,input().split())) for i in range(4)]
result = []

def dfs(i,j,comb):
    dj = [1,0,-1,0]
    di = [0,-1,0,1]
    if len(comb) == 7:
        result.append(comb)
        return
    for k in range(4):
        si = i + di[k]
        sj = j + dj[k]
        if si>=0 and si<4 and sj>=0 and sj<4:
            dfs(si, sj,comb+str(num_list[si][sj]))


for i in range(4):
    for j in range(4):
        comb = str(num_list[i][j])
        dfs(i, j,comb)

print(len(set(result)))
