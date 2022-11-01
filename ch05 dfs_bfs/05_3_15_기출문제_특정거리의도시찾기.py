from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    vin, vout = map(int, sys.stdin.readline().split())
    graph[vin - 1].append(vout)
    
# d[new] = min(d[new], d[last] + 1)
dist = [n] * (n + 1)
dist[x] = 0
visited = [False] * (n + 1)

queue = deque([x])
visited[x] = True
while queue:
    curr = queue.popleft()
    for i in range(len(graph[curr - 1])):
        item = graph[curr-1][i]
        if visited[item] == False:
            queue.append(item)
            visited[item] = True
            dist[item] = dist[curr] + 1
            
answer = []
for i in range(1, len(dist)):
    if dist[i] == k:
        answer.append(i)
        print(i, end=' ')

if len(answer) == 0:
    print('-1')
