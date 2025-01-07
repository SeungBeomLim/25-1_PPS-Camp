# A206. 숨바꼭질 6 - Baekjoon

import math
from functools import reduce

N, S = map(int, input().split())

A = list(map(int, input().split()))

differences = [abs(pos - S) for pos in A]

max_d = reduce(math.gcd, differences)

print(max_d)
