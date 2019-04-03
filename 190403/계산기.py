T = int(input())
for tc in range(1,T+1):
    arr = list(input().split())
    goal = int(input())
    cal = []
    for i in range(10):
        if arr[i] == '1':
            cal.append(i)
    print(cal)
# 미완성