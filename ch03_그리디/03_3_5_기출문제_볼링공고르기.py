
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# ball = {무게:공개수, ...}
ball = []
count = 1
last = data[0]
for i in range(1, len(data)):
    if last == data[i]:
        count += 1
    else:
        ball.append((last, count))
        last = data[i]
        count = 1
ball.append((last, count))

answer = 0
for i in range(len(ball)):
    for j in range(i + 1, len(ball)):
        answer += ball[i][1] * ball[j][1]

print(answer)