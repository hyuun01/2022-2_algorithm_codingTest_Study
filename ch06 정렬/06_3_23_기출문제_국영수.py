import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    name, k, e, m = sys.stdin.readline().split()
    data.append((name, int(k), int(e), int(m)))

data.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(data[i][0])
    