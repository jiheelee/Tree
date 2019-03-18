def swim(n, s): #월, 비용
    global d, m, m3, y, minV
    if (n>=12):
        if s < minV:
            minV = s
        return
    else:

        swim(n+1, s + number[n] * d)
        m_fee = 0 if number[n] == 0 else m
        swim(n+1, s + m_fee)
        if n <= 9:
            m3_fee = m3 if 0 in (number[n],number[n+1],number[n+2]) else 0
        elif n==10:
            m3_fee = m3 if 0 in (number[n], number[n + 1]) else 0
        else:
            m3_fee = m3 if number[n] != 0 else 0
        swim(n+3, s + m3)






T = int(input())
for tc in range(1,T+1):
    d, m, m3, y = map(int,input().split())
    number = list(map(int,input().split()))
    minV = y
    fee = []
    swim(0,0)
    print('#{} {}'.format(tc,minV))
