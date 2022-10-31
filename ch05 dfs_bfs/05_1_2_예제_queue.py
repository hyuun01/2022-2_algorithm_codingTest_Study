from collections import deque
queue = deque()
queue.append(5)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)

print(queue) # 처음 들어온 원소부터 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력

# queue -> list
list_queue = list(queue)
