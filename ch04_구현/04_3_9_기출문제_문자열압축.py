def solution(s):
    answer = len(s)
    
    for i in range(1, int(len(s)/2) + 1):
        # length_n = len(s)
        last = s[:i]
        num = 1
        compressed = ""
        
        for j in range(i, len(s), i):
            if last == s[j:j+i]:
                num += 1
            else:
                if num > 1:
                    # length_n += 1 - (num - 1) * i
                    compressed += str(num) + last
                else:
                    compressed += last
                num = 1
                last = s[j:j+i]    
        #if num > 1:
            # length_n += 1 - (num - 1) * i # 이 식이 잘못됐었음 -> 그냥 컴퓨터공학적으로 직접 압축한 후 추후 계산하기!!
        compressed += str(num) + last if num > 1 else last 
        answer = min(answer, len(compressed))    
        #if length_n < answer:
        #    answer = length_n
            
    return answer