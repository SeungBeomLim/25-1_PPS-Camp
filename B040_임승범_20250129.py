# B040. DNA 발견 - Baekjoon

import sys

def min_mutations_to_all_A(n, s):
    INF = int(1e9)
    
    # 현재와 이전 상태 변수
    prev_A, prev_B = (0, 1) if s[0] == 'A' else (1, 0)

    for i in range(1, n):
        if s[i] == 'A':
            cur_A = min(prev_A, prev_B + 1)
            cur_B = min(prev_A + 1, prev_B + 1)
        else:
            cur_A = min(prev_A + 1, prev_B + 1)
            cur_B = min(prev_A + 1, prev_B)

        prev_A, prev_B = cur_A, cur_B  # 현재 값을 이전 값으로 업데이트

    return prev_A


# 입력 처리
n = int(sys.stdin.readline().strip())  # DNA 길이
s = sys.stdin.readline().strip()  # DNA 문자열

# 결과 출력
print(min_mutations_to_all_A(n, s))