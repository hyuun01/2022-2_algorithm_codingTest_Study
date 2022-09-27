n, m = map(int, input().split())
data = list(map(int, input().split()))
array = [0]*11
for x in data:
    array[x] += 1

answer = 0
for i in range(1, 11):
    n -= array[i]
    answer += array[i]*n

print(answer)
    