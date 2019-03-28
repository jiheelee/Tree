def npr(n, k):
    if n==k:
        if(p[0]+1 == p[1] and p[1]+1==p[2]): #run
            r = 1
    else:
        for i in range(k, n):
            p[i], p[k] = p[k], p[i]
            npr(n, k + 1)
            p[i], p[k] = p[k], p[i]
p = [1,2,3,4,5]
npr(5, 0)
