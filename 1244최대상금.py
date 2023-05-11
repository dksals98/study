num = int(input())

def dfs(n):
    global maxnum
    if n == change:
        maxnum = max(maxnum, int("".join(case_list)))
        return

    for i in range(L-1):
        for j in range(i+1, L):
            case_list[i], case_list[j] = case_list[j], case_list[i]
            ckd = int("".join(case_list))
            if (n, ckd) not in visited:
                dfs(n+1)
                visited.append((n, ckd))
            case_list[i], case_list[j] = case_list[j], case_list[i]

for i in range(num):
    case, change = input().split()
    change = int(change)
    case_list = []
    visited = []
    maxnum = 0
    for ch in case:
        case_list.append(ch)
    L = len(case_list)
    dfs(0)
    print(f'#{i+1} {maxnum}')

