pos = input()
answer = 0

c = ord(pos[0]) - ord('a') + 1
r = int(pos[1])

# (rDir, cDir)
dir = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

for x in dir:
    nextR = r + x[0]
    nextC = c + x[1]
    if not(nextR < 1 or nextR > 8 or nextC < 1 or nextC > 8):
        answer += 1

print(answer)