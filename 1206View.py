for T in range(10):
    num = int(input())
    building = []
    building = list(map(int, input().split()))

    mylist = [[0] * 255 for _ in range(num)]
    dx = [1, -1]

    x, y = 0, 0
    count = 0

    for i in range(num):
        for j in range(building[i]):
            mylist[i][j] = 1

    for i in range(num-2):
        for j in range(255):
            k = i+2
            if mylist[k][j] == 1 and mylist[k+1][j] == 0 and mylist[k+2][j] == 0 and mylist[k-1][j] == 0 and mylist[k-2][j] == 0:
                count += 1

    print("#"+str(T+1)+" "+str(count))