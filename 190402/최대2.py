def change(n,k):
    global maxV,cnt
    global length
    if n==k:
       res.add(int(''.join(num)))
    else:
        for i in range(length-1):
            for j in range(i+1,length):
                if int(num[j]) >= int(num[i]):
                    num[i],num[j] = num[j],num[i]
                    change(n+1,k)
                    cnt+=1
                    num[i], num[j] = num[j], num[i]
import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    num, k = map(int,input().split())
    num = list(str(num))
    maxV = 0
    length = len(num)
    res = set()
    cnt = 0
    change(0,k)
    # print(max(list(res)))
    print(cnt)