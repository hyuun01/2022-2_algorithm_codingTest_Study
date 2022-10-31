n = input()

# 4 : 0,1 / 2,3
front_n = n[:int(len(n)/2)]
back_n = n[int(len(n)/2):]

num_fn = sum(int(front_n[i]) for i in range(len(front_n)))
num_bn = sum(int(back_n[i]) for i in range(len(back_n)))

'''
print(front_n)
print(back_n)
print(num_fn)
print(num_bn)
'''

if num_fn == num_bn :
    print("LUCKY")
else:
    print("READY")
