str = input()

# count 는 0인 구간 개수
count_0 = 0
count_1 = 0

mark = '1'

for i in range(len(str)):
    # 새로운 0구간 시작 시 count_0 ++
    if mark == '1' and str[i] == '0':
        count_0 += 1
    # 새로운 1구간 시작시 count_1 ++
    elif mark == '0' and str[i] == '1':
        count_1 += 1
    mark = str[i]
            
print(min(count_0, count_1))