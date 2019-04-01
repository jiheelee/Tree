def make_set(x):
    p[x] = x
def find_set(x):
    while p[x] != x:
        x = p[x]
    return x
def union(x,y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())

    k_list = []
    for i in range(E):
        k_list.append(list(map(int,input().split())))

    k_list.sort(key=lambda x:x[2])
    p = [0] * (V+1)
    for i in range(V+1):
        make_set(i)
    res = 0
    for j in k_list:
        if find_set(j[0]) != find_set(j[1]):
            res += j[2]
            union(j[0],j[1])
    print('#{} {}'.format(tc,res))
    print(p)

