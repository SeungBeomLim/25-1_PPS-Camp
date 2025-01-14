# A215. 부호 - Baekjoon

for _ in range(3):
    N = int(input())
    S = 0
    
    for i in range(N):
        S += int(input())

    if S > 0:
        print('+')
    elif S < 0:
        print('-')
    else:
        print('0')