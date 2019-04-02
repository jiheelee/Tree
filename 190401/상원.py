def make_set(x):
    p[x] = x
def find_set(x):
    while p[x] != x:
        x = p[x]
    return x
def union(x,y):
    p[find_set(y)] = find_set(x)

import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    p = [0] * (N+1)
    for i in range(N+1):
        make_set(i)
    print(p)
    for i in range(M):
        a, b = map(int,input().split())
        union(a,b)

    print(p)

