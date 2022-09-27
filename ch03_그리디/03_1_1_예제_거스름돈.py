n = int(input())
result = 0

coin_set = [500, 100, 50, 10]

for item in coin_set:
    if n == 0:
        break
    result += n // item
    n %= item
    
print(result)