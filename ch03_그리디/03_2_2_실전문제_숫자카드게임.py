n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    item = min(data)
    
    # result = max(result, item)
    if result < item :
        result = item
        
print(result) 