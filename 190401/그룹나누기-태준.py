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
    N, M = map(int,input().split())
    p = [0] * (N+1)
    arr = list(map(int,input().split()))
    for i in range(1,N+1):
        make_set(i)
    for i in range(M):
        union(arr[2*i], arr[2*i+1])

    res = set()
    for i in range(1,len(p)):
        res.add(find_set(p[i]))
    print('#{} {}'.format(tc,len(res)))