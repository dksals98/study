T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for test_case in range(1, T + 1):
    num = int(input())
    frame = [[0]*num for _ in range(num)]
    print("#"+str(test_case))

    x, y = -1, 0
    move = 1
    val = 1
    twice = 0

    for _ in range(num):
        x = x + 1
        frame[x][y] = val
        val += 1
    count = num

    while count != 0:
        if twice == 0:
            count = count - 1
            twice = 2

        for i in range(count):
            x = x + dx[move]
            y = y + dy[move]
            frame[x][y] = val
            val += 1

        move = (move + 1) % 4
        twice -= 1

    for i in range(num):
        for j in range(num):
            print(frame[j][i], end=" ")
        print()