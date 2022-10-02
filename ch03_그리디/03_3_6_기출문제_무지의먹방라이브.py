def solution(food_times, k):
    # 틀린 이유 : -1 반환하는 케이스
    if sum(food_times) <= k:
        return -1
    
    answer = 0
    arr = []
    for i in range(len(food_times)):
        arr.append([i+1, food_times[i]])
    
    arr.sort(reverse=True, key=lambda x:x[1])

    length = len(arr)
    time = 0
    eaten = 0
    while True:
        min_value = arr[-1][1]
        add_value = (min_value - eaten) * length
        if time + add_value > k: break
        time += add_value
        eaten = min_value
        while arr[-1][1] == min_value:
            del arr[-1]
            length -= 1
        
    arr.sort(key=lambda x: x[0])
    
    # for left loop
    leftLoop = (k - time) // length
    if time + leftLoop * length > k:
        # print('Logic Error')
        return 0
    eaten += leftLoop
    time += leftLoop * length
    
    # for r value 
    left = k - time
    answer = arr[left][0]   
    
    return answer
