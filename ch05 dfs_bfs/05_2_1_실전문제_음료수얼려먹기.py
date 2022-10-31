# bfs 풀이
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(input())

visited = [[False]*m for i in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0' and not visited[i][j]:
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            while queue:
                curr = queue.popleft()
                dir = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
                for d in dir:
                    r = curr[0] + d[0]
                    c = curr[1] + d[1]
                    if r>=0 and r<n and 0<=c and c<m and not visited[r][c] and graph[r][c] == '0' :
                        queue.append((r, c))
                        visited[r][c] = True
            answer += 1
print(answer)
