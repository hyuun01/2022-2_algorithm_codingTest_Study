
def solution(N, stages):
    answer = []
    rate = [[i, 0, 0] for i in range(N+2)]   # i번째 stage가 answer[i][2]명
    data = [(x, stages[x]) for x in range(len(stages))]
    
    data.sort(key=lambda x: x[1])
    stagenum = data[0][1]
    rate[stagenum][1] = 1
    for i in range(1, len(stages)):
        if data[i][1] == stagenum:
            rate[stagenum][1] += 1
        else:
            while data[i][1] > stagenum:
                stagenum += 1
            rate[stagenum][1] += 1
    
    pplsum = len(stages)
    for i in range(1, N + 1):
        rate[i][2] = rate[i][1] / pplsum
        pplsum -= rate[i][1]
        if pplsum == 0:
            break
    
    rate = rate[1:N+1]
    rate.sort(key=lambda x : (-x[2], x[0]))
    
    for x in rate:
        answer.append(x[0])
    
    return answer

