arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

result = []
for i in range(3):
    for j in range(3):
        leftup = 0
        rightup = 0
        leftdown = 0
        rightdown = 0
        for m in range(i+1):
            for n in range(j+1):
                leftup += arr[m][n]
        for m in range(i+1):
            for n in range(j+1,4):
                rightup += arr[m][n]
        for m in range(i+1,4):
            for n in range(j+1):
                leftdown += arr[m][n]
        for m in range(i+1,4):
            for n in range(j+1,4):
                rightdown += arr[m][n]
        print(leftup,rightup,leftdown,rightdown)