from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

starts = []
emptys = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            starts.append((i, j))
        elif graph[i][j] == 0:
            emptys.append((i, j))

answer = 0
for i in range(len(emptys)):
    for j in range(i+1, len(emptys), 1):
        for k in range(j+1, len(emptys), 1):
            queue = deque()
            newgraph = [[graph[r][c] for c in range(m)] for r in range(n)]
            newgraph[emptys[i][0]][emptys[i][1]] = 1
            newgraph[emptys[j][0]][emptys[j][1]] = 1
            newgraph[emptys[k][0]][emptys[k][1]] = 1
            for x in starts:
                # dfs -> fill with 1
                queue.append(x)
                while queue:
                    curr = queue.popleft()
                    dx = [1, -1, 0, 0]
                    dy = [0, 0, 1, -1]
                    for ind in range(4):
                        nx = dx[ind] + curr[0]
                        ny = dy[ind] + curr[1]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if newgraph[nx][ny] == 0:
                            queue.append((nx, ny))
                            newgraph[nx][ny] = 2
                
            count = 0
            for li in newgraph:
                for item in li:
                    if item == 0:
                        count += 1
            answer = max(answer, count)

print(answer)
            