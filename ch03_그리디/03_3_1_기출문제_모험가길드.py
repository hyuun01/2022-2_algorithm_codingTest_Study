n = int(input())

data = list(map(int, input().split()))

data.sort()
num = len(data)

result = 0

while num > 0 :
    item = data[num-1]
    result += 1
    num -= item

if num < 0 :
    result -= 1

print(result)