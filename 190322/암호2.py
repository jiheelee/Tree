import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    password = [input() for i in range(N)]
    a_list = []
    for i in range(N):
        c = ''
        st = 0
        ed = 0
        j = 0
        if password[i] == '0' * M:
            pass
        else:
            while j<M-1 and password[i][j] == '0':
                j += 1
                st = j

            j = M-1
            if st != M-1:
                while j>=1 and password[i][j] == '0':
                    j -= 1
                    ed = j
                c += password[i][st:ed+1]
                a_list.append(c)
                n = i
                while password[n][st:ed+1] != '0' * (ed-st+1) and n<N:
                    password[n] = password[n][0:st] + '0' * (ed-st+1) + password[n][ed+1:-1]
                    n += 1

    result = []
    for k in range(len(a_list)):
        sixteen = a_list[k]
        print(sixteen)
        # print(len(sixteen))
        s_list = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101',"E":'1110','F':'1111'}
        two = ''

        for s in sixteen:
            for key,val in s_list.items():
                    if key == s:
                        two += val
        print(two)
        p = len(two)
        print(p)
        length = p//56
        print(length)

        num_list = []
        end = 0
        for i in range(p-1,0,-1):
            if two[i]!= '0':
                end = i
                break

        two = two[0:end+1]


        if len(two) < 56*length:
            two = (56*length-len(two)) * '0' + two
        if len(two) > 56 * length:
            two = two[len(two)-56*length::]

        for i in range(8):
            num_list.append(two[7*i*length:7*i*length+7*length])

        dic = {'0001101':'0','0011001':'1','0010011':'2','0111101':'3','0100011':'4','0110001':'5','0101111':'6','0111011':'7','0110111':'8','0001011':'9'}
        code = ''
        for i in range(8):
            c = ''
            for j in range(7*length):
                if j % length == 0:
                    c += num_list[i][j]
            for key,val in dic.items():
                if c == key:
                    code += val
        even = 0
        odd = 0

        for i in range(8):
            if i%2:
                odd += int(code[i])
            else:
                even += int(code[i])
        if (even*3 + odd) % 10 == 0:
            result.append(even + odd)

    print(result)
