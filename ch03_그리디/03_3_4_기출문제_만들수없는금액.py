n = int(input())
coin_type = list(map(int, input().split()))
coin_type.sort()

# 1

# [1, 1, 1||||, 5, 8]
# sum = 3 < 5
# 3, 4, 5, 6, 7


# sum = (c_1 + c_2 + ... + c_n-1) 까지는 만들 수 있다 
# -> sum >= c_n 이면 c_1 + ... + c_n까지는 만들 수 있다.
sum = 1
for x in coin_type:
    if sum < x:
        break
    else:
        sum += x
        
answer = sum + 1
print(answer)















'''
# 1차 풀이 : 틀림
# -> last 값이 계속 0으로 됨, 두번째 for-loop가 제대로 안 돌아감
def findAnswer():
    n = int(input())
    coin_type = list(map(int, input().split()))
    coin_type.sort()
    answer = 1

    # if 가장 작은 코인 단위가 1 -> answer = 1
    # else 최소값은 n + 1부터 시작
    if coin_type[0] == 1:
        count = 0
        last = 0
        new = 0
        for i in range(len(coin_type)):
            count += coin_type[i]
            for j in range(i + 1, len(coin_type)):
                new = count + coin_type[j]
                if last + 1 != new:
                    answer = last + 1
                    break
                else:
                    last = new

    
    print(answer)
'''