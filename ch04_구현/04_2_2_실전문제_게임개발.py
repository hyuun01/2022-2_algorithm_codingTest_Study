# n x m map
n, m = map(int, input().split())

# (a, b)에 d쪽을 바라보고 서 있는 캐릭터
a, b, d = map(int, input().split())

# 0 : 육지, 1 : 바다
map = []
for _ in range(n):
    data = list(map(int, input().split()))
    map.append(data)

answer = 0

while True:
    newd = (d + 3) % 4   
    

print(answer)