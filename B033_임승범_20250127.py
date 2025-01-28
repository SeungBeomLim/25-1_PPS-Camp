# B033. 전자레인지 - Baekjoon

T = int(input())

A, B, C = 300, 60, 10 # 5분, 1분, 10초

if T % C != 0:
    print(-1)
else:
    count_A = T // A
    T %= A
    count_B = T // B
    T %= B
    count_C = T // C

    print(f"{count_A} {count_B} {count_C}")
        