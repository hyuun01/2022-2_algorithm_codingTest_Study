n = int(input())
data = []
for _ in range(n):
    x, y = input().split()
    data.append((x, int(y)))

data.sort(key=lambda x: x[1])
for i in range(n):
    print(data[i][0], end=' ')