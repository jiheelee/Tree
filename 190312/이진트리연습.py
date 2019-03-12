def vlr(n):
    if(n>0):
        print(n, end=' ')
        vlr(ch1[n])
        vlr(ch2[n])

def lvr(n):
    if(n>0):
        lvr(ch1[n])
        print(n, end=' ')
        lvr(ch2[n])
    return

def dlr(n):
    print(n, end= ' ')
    if(ch1[n]>0):
        dlr(ch1[n])
    if(ch2[n]>0):
        dlr(ch2[n])


import sys
sys.stdin = open('input.txt','r')


V, E = map(int,input().split())
node = list(map(int, input().split()))

ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

for i in range(E):
    n1 = node[i*2]
    n2 = node[i*2+1]
    if ch1[n1] == 0:
        ch1[n1] = n2
    else:
        ch2[n1] = n2

print(ch1,'\n', ch2)
print(vlr(1))
