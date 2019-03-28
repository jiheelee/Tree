def f(n,k,e,c):
    global minV
    if n==k:
        if minV > c:
            minV = c
    else:
        if e>0:
            f(n+1,k,e-1,c) #통과

        f(n+1,k,bat[n]-1,c+1)#교체

N = list(map(int,input().split()))
num = N[0]
bat = N[1::]
minV = num
f(2,num,bat[1]-1,0)
