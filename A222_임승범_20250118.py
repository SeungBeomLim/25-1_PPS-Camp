# A222. 이항 계수 1 - Baekjoon

import math

N, K = map(int, input().split())

b_c = math.factorial(N) // (math.factorial(K) * math.factorial(N - K))

print(b_c)