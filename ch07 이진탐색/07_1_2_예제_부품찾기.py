import sys

n = int(input())
data1 = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
data2 = list(map(int, sys.stdin.readline().rstrip().split()))

data1.sort()

def bin_search(data, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        elif data[mid] > target:
            end = mid - 1
    return False

for item in data2:
    if bin_search(data1, item, 0, len(data1)):
        print('yes')
    else:
        print('no')
