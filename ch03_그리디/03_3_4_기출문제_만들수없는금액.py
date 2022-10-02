# 교재 풀이
n = int(input())
coin_type = list(map(int, input().split()))
coin_type.sort()
answer = 1

# 왜 이 과정 거치면 답인지 이해 안 됨...
for x in coin_type:
    if answer < x:
        break
    else:
        answer += x

print(answer)


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
    