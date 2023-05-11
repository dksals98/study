T = int(input())

for case in range(T):
    maxkill = 0
    N, M = map(int, input().split())
    mylist = [[0] * N for i in range(N)]

    for t in range(N):
        mylist[t] = list(map(int, input().split()))

    for i in range(N-M+1):
        for j in range(N-M+1):
           kill = 0
           for k in range(M):
              for l in range(M):
                  kill += mylist[i+k][j+l]
           maxkill = max(maxkill, kill)

    print(f'#{case+1} {maxkill}')
