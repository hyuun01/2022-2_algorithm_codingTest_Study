n, k = map(int, input().split())

result = 0

while n > 1 :
    result += n % k
    if n > 1 :
        n //= k
        result += 1
    
print(result)
