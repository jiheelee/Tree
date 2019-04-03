import sys
sys.stdin = open('input.txt','r')
T = int(input()) + 1
for tc in range(1, T):
    cnt = 0
    N, M = input().strip().split()
    M = int(M)
    now = set()
    after = set()
    now.add(N)
    for i in range(M):
        while now:
            s = list(str(now.pop()))
            for n in range(len(N)):
                for m in range(n + 1, len(N)):
                    if s[n] <= s[m]:
                        s[n], s[m] = s[m], s[n]
                        after.add(int("".join(s)))
                        cnt+=1
                        s[m], s[n] = s[n], s[m]
        now, after = after, now

    # print("#{} {}".format(tc, max(map(int, now))))
    print(cnt)