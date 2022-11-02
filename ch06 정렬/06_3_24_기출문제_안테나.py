n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1)//2])

'''
anslist = []
for i in range(n):
    pivot = data[i]
    count = 0
    for j in range(n):
        count += abs(data[j]-pivot)
    anslist.append((count, pivot))

anslist.sort(key=lambda x: x[0])
print(anslist[0][1])


'''