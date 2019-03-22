T = int(input())
for tc in range(1,T+1):
    N, K = input().split()
    num = 0
    result = ""
    for n in range(int(N)):
        if K[n] == "A":
            num = 10
        elif K[n] == "B":
            num = 11
        elif K[n] == "C":
            num = 12
        elif K[n] == "D":
            num = 13
        elif K[n] == "E":
            num = 14
        elif K[n] == "F":
            num = 15
        else:
            num = int(K[n])
        for i in range(3,-1,-1):
            if num // (2 ** i):
                result += "1"
                num = num % (2**i)
            else:
                result += "0"


    print(result)


