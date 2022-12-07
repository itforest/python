def f(*x): # *: 인자수가 정해지지 않음을 의미
    sum = 0
    multiple = 1
    for val in x:
        sum += val
        multiple *= val
    return sum,multiple
    S, M = f(1,2,3,4,5)

print(S,M) # 출력은 15, 120
