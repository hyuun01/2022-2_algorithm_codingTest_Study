n, x = map(int, input().split())
data = list(map(int, input().split()))

def bin_max_pos_search(dlist, start, end, key):
    answer = -1
    while start <= end:
        mid = (start+end)//2
        if dlist[mid] <= key:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer

def bin_min_pos_search(dlist, start, end, key):
    answer = -1
    while start <= end:
        mid = (start+ end)//2
        if dlist[mid] < key:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    return answer

min_pos = bin_min_pos_search(data, 0, len(data) - 1, x)
max_pos = bin_max_pos_search(data, 0, len(data) - 1, x)
if data[min_pos] == x and data[max_pos] == x:
    print(max_pos - min_pos + 1)
else:
    print(-1)
