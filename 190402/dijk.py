def dij(s, v):
    u = [s]
    for i in range(1,v+1):
        d[i] = adj[s][i]

    while len(u) != v:
        minV = 1000000
        w = 0
        for i in range(1,v+1):
            if i not in u:
                if d[i]<minV:
                    minV = d[i]
                    w = i
        u.append(w)
        for i in range(1, v+1):
            if w!=i and adj[w][i] != 1000000:
                d[i] = min(d[i],d[w] + adj[w][i])



import sys
sys.stdin = open('input.txt','r')
V,E =map(int,input().split())
adj = [[1000000]*(V+1) for i in range(V+1)]
for i in range(V+1): #출발 도착이 같으면 0
    adj[i][i] = 0
for i in range(E): #인접 정보 추가
    n1,n2,w = map(int, input().split())
    adj[n1][n2] = w
s = 1
d = [0] * (V+1)
dij(1,V)
print(d)
