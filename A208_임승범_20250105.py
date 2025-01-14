# A208. 골드바흐 파티션 - Baekjoon
# 에라토스테네스의 체를 이용해서 소수를 구한 후, 입력 수 - 소수 = 소수가 되는지 판별.

prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

T = int(input())

for _ in range(T):
    count = 0
    N = int(input())
    for i in prime:
        if i >= N:
            break
        if not check[N - i] and i <= N-i:  # 순서만 다른거 counting 하지 않기 위해
            count += 1
    print(count)
