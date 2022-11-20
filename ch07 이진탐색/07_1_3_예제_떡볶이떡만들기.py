import sys

n, h = map(int, input().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()


start = 0
end = max(data)
sum_height = 0
height = 0
while start <= end:
    mid = (start + end) // 2
    sum_height = sum(max(x - mid, 0) for x in data)
    # if sum_height == h:
    #     height = mid
    #     break
    if sum_height >= h:
        height = mid
        start = mid + 1
    elif sum_height < h:
        end = mid - 1
print(height)

        

'''
count = 1
sum_height = 0
last_height = data[0]
while sum_height < h:
    sum_height += count * (last_height - data[count])
    last_height = data[count]
    count += 1
    
print(last_height)
'''
