n = int(input())
data= list(map(int, input().split()))

def bin_search(dlist, start, end):
    while start <= end:
        mid = (start+end)//2
        if data[mid] == mid:
            return mid
        elif data[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(bin_search(data, 0, len(data) - 1))
