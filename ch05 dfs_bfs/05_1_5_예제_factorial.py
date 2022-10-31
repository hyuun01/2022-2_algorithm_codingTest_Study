def fact(n):
    if n < 1:
        return 1
    else:
        return n * fact(n-1)

def iterfac(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer