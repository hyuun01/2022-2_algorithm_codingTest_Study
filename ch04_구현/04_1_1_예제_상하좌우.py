def route(n, moves):
    dest = [1, 1]
    next = [1, 1]
    
    dir = {'R':(0, 1), 'L':(0, -1), 'U':(-1, 0), 'D':(1, 0)}
    for d in moves:
        next[0] = dest[0] + dir[d][0]
        next[1] = dest[1] + dir[d][1]
        if next[0] > 0 and next[0] <= n and next[1] > 0 and next[1] <= n:
            dest[0], dest[1] = next[0], next[1]

    return dest

n = int(input())
moves = list(input().split())
answer = route(n, moves)
print(answer[0], answer[1])    
    