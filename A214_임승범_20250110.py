# 214. Darius님 한타 안 함? - Baekjoon

K, D, A = map(int, input().split('/'))

print("hasu" if K + A < D or D == 0 else "gosu")