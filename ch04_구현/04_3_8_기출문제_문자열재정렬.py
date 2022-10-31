s = input()
data = list(s[i] for i in range(len(s)))

data.sort()
index = 0
for i in range(len(data)):
    if 'A' <= data[i] <='Z':
        index = i
        break
fd = data[:index]
bd = data[index:]
data = bd + fd
print(''.join(data))
