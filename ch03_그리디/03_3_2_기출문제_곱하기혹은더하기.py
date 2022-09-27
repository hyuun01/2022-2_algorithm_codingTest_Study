n = input()

length = len(n)

result = int(n[0])

for i in range(1, length):
    item = int(n[i])
    # 0이거나 1일때는 더하는게 유리
    # 그 외는 곱하는게 유리
    if item <= 1 or result <= 1:
        result *= item
    else:
        result += item

print(result)
