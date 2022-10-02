# Lake Counting
# http://poj.org/problem?id=2386

N = int(input())
M = int(input())
field = [list(input()) for i in range(M)]

def dfs(n, m):
    # boundary judgement needs to be more simple
    range_x = range(n-1, n+2)
    range_y = range(m-1, m+2)
    
    if n-1 < 0: range_x = range(n, n+2)
    if n+1 >= N: range_x = range(n-1, n+1) 
    if m-1 < 0: range_y = range(m, m+2)
    if m+1 >= M: range_y = range(m-1, m+1)

    for i in range_x:
        for j in range_y:
            if field[i][j] == 'W':
                field[i][j] = '.'
                dfs(i, j)
    return

def solve():
    count = 0
    for i in range(0, N):
        for j in range(0, M):
            if field[i][j] == 'W':
                dfs(i, j)
                count += 1
    return count

print(solve())