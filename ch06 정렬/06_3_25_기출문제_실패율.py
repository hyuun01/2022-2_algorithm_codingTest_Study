def solution(N, stages):
    answer = []
    data = [(x, stages[x]) for x in range(len(stages))]
    
    data.sort(key=lambda x: x[1])
    stagenum = data[0][1]
    ind = 0
    answer.append(0)
    for i in range(1, len(stages)):
        if data[i][1] == stagenum:
            answer[ind] += 1
            continue
        while data[i][1] > stagenum:
            stagenum += 1
        answer.append(0)
        ind += 1
    
    
    return answer
