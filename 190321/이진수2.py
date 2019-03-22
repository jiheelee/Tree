T = int(input())
for tc in range(1,T+1):
    num = float(input())
    cnt = 1
    result = ""
    while str(num)[-1]!="0":
        if cnt == 13:
            result = "overflow"
            break
        num = num * 2
        result += str(num)[0]
        cnt += 1
        print(num)
    print(result)