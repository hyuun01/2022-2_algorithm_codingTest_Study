n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()
max_1 = data[n-1]
max_2 = data[n-2]

count = m // (k + 1)

result = max_1 * count * k + max_2 * count + max_1 * (m % (k + 1))
        
print(result)