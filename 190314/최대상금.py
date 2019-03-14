N, K = map(int,input().split())
N = str(N)
num_list = []
num = []
for n in N:
    num_list.append(int(n))
for n in N:
    num.append(int(n))
idx_list = []
for i in range(len(N)):
    idx_list.append(i)
# print(idx_list)
# print(num_list)

for i in range(len(N)-1,0,-1):
    for j in range(0,i):
            if num_list[j] <= num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                idx_list[j], idx_list[j+1] = idx_list[j+1], idx_list[j]
t = K
print(idx_list)
print(num)
for k in range(K):
    if k == idx_list[k]:
        pass
    else:
        num[k], num[idx_list[t-k-1]] = num[idx_list[t-k-1]], num[k]
        idx_list[k], idx_list[idx_list[t-k-1]] = idx_list[idx_list[t-k-1]], idx_list[k]
        t -= 2
print(num)

