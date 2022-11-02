import heapq

n = int(input())
heap = []
for _ in range(n):
    cardnum = int(input())
    heapq.heappush(heap, cardnum)
    
ans = 0
while len(heap) > 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap, x+y)
    ans += x + y

print(ans)
    
