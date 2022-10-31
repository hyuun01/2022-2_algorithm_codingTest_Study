from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
answer = n * m
queue = deque()
queue.append((0, 0, 1))
while queue:
    curr = queue.popleft()
    if curr[0] == (n -1) and curr[1] == (m - 1):
        answer = min(answer, curr[2])
        continue    
    graph[curr[0]][curr[1]] = 0
    dic = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for d in dic:
        r = curr[0] + d[0]
        c = curr[1] + d[1]
        if r >= 0 and r < n and c >= 0 and c < m and graph[r][c] == 1:
            queue.append((r, c, curr[2]+1))
            graph[r][c] = 0

print(answer)