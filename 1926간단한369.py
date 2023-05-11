T = int(input())

for i in range(1, T+1):
    temp = list(str(i))
    for j in range(len(temp)):
        if temp[j] == '3' or temp[j] == '6' or temp[j] == '9':
            temp[j] = '-'

    if "-" in temp:
        num = temp.count('-')
        if num == 1:
            temp = '-'
        if num == 2:
            temp = '--'
        if num == 3:
            temp = '---'

    temp = ''.join(temp)
    print(temp, end=" ")
