import sys
n, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
update = [[k+1]*n for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))
s, x, y = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# during s seconds
for _ in range(s):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                for dind in range(4):
                    nx = i + dx[dind]
                    ny = j + dy[dind]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if graph[nx][ny] != 0:
                        update[i][j] = min(update[i][j], graph[nx][ny])
    for i in range(n):
        for j in range(n):
            graph[i][j] = update[i][j] if graph[i][j] == 0 and update[i][j] != k + 1 else graph[i][j]
                
if graph[x-1][y-1] == k+1:
    print(0)
else:
    print(graph[x-1][y-1])
