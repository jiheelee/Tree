import sys
sys.stdin = open('input.txt','r')

def bfs(i,j):
    q = []
    di = [0,-1,0,1]
    dj = [1,0,-1,0]
    q.append(i)
    q.append(j)
    while q:
        i = q.pop(0)
        j = q.pop(0)
        for k in range(4):
            si = i + di[k]
            sj = j + dj[k]
            
