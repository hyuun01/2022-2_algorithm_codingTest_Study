n = int(input())
answer = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if i % 10 == 3 or (i // 10) == 3 or j % 10 == 3 or (j // 10) == 3 or k % 10 == 3 or (k // 10) == 3 :
                answer += 1
                
print(answer)