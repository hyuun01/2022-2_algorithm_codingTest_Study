def solution(key, lock):
    answer = True
    m = len(key)
    n = len(lock)
    rot0key = key
    rot1key = [[key[c][m - r] for c in range(m)]for r in range(m)]
    rot2key = [[key[m - c][m - r] for c in range(m)]for r in range(m)]
    rot3key = [[key[m - c][r] for c in range(m)]for r in range(m)]
    keys = [rot0key, rot1key, rot2key, rot3key]
    
    for skey in keys:
        # key 넣어보기
        # if match -> answer=True break
        answer = True
        for r in range(n):
            for c in range(n):
                for i in range(n):
                    if answer == False:
                        break
                    for j in range(n):
                        if lock[i][j] + skey[i][j] != 1:
                            answer = False
                            break
                if answer == True:
                    return answer
                
                    
    return answer