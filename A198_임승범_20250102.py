# A198. 파닭파닭 - Baekjoon

# 입력 받기
S, C = map(int, input().split())  # 파의 개수(S)와 주문받은 파닭의 수(C)
pa_lengths = [int(input()) for _ in range(S)]  # S개의 파의 길이 입력

# 이진 탐색을 이용한 최대 파 길이 계산
start, end = 1, max(pa_lengths)  # 최소 1부터 최대 파 길이까지
max_length = 0

while start <= end:
    mid = (start + end) // 2  # 중간값 계산
    chicken_count = 0  # 만들 수 있는 파닭의 수
    used_length = 0  # 사용된 파 길이

    # 만들 수 있는 파닭의 수와 사용된 파 길이 계산
    for length in pa_lengths:
        chicken_count += length // mid
        used_length += (length // mid) * mid

    if chicken_count >= C:
        max_length = mid  # 가능한 파 길이 저장
        start = mid + 1  # 더 큰 파 길이 탐색
    else:
        end = mid - 1  # 더 작은 파 길이 탐색

# 남은 파의 양 계산
total_length = sum(pa_lengths)
remaining_length = total_length - (max_length * C)

# 결과 출력
print(remaining_length)
