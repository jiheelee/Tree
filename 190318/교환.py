import sys
sys.stdin = open('input.txt','r')

def f(n, k, c):
    global t
    global check
    if (n==k):
        k_list.append(int("".join(card)))
        t = c
        return
    if (c==0):
        c_list.append(int("".join(card)))
        check = 1
        return
    else:
        for i in range(n, k):
            card[n], card[i] = card[i], card[n]
            if(i==n):
                f(n+1,k,c)
            else:
                f(n+1,k,c-1)
            card[n], card[i] = card[i], card[n]




T = int(input())
for tc in range(1, T+1):
    num, c = input().split()
    card = list(num)
    g = []
    for i in card:
        if i not in g:
            g.append(i)

    k_list = []
    c_list = []
    t = 0
    check = 0
    f(0, len(card), int(c))
    if c_list:
        if max(c_list)<max(k_list):
            check = 0
    if check == 1:
        result = max(c_list)
    else:
        if len(g) != len(card):
            result = max(k_list)
        else:
            if t % 2 == 0:
                result=max(k_list)
            else:
                string = str(max(k_list))
                string = list(string)
                string[-1],string[-2] = string[-2],string[-1]
                result = int(''.join(string))

        print(result)

