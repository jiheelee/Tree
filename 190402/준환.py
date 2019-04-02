# from itertools import permutations
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     permu = list(permutations(arr,N))
#     cnt = 0
#     for i in range(len(permu)):
#         for m in range(1<<N):
#             k = []
#             for n in range(N+1):
#                 if m & (1<<n):
#                     k.append(permu[i][n])
#             left = 0
#             right = 0
#             c = 0
#             for p in range(N):
#                 if permu[i][p] in k:
#                     left += permu[i][p]
#                 else:
#                     right += permu[i][p]
#                 if right > left:
#                     c =1
#                     break
#             if c==0:
#                 cnt += 1
#
#     print('#{} {}'.format(tc,cnt))
def f(n,k,l,r,ld,rd) :
    if l < r :
        return 0
    if n == k :
        return 1
    elif d[ld][rd] != -1 :
        return d[ld][rd]
    else :
        sum = 0
        for i in range(N):
            if u[i] == 0 :
                u[i] = 1
                sum += f(n+1,k,l+Weights[i],r,ld+(1<<i),rd)
                sum += f(n+1,k,l,r+Weights[i],ld,rd+(1<<i))
                u[i] = 0
        d[ld][rd] = sum
        return sum


T = int(input())+1
for tc in range(1,T):
    N = int(input())
    Weights = list(map(int,input().strip().split()))
    d = [[-1]*(2**N) for _ in range(2**N)]
    u = [0]*N
    print("#{} {}".format(tc,f(0,N,0,0,0,0)))