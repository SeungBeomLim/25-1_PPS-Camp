# B039. 추 정렬하기 - Baekjoon
# 어려운 문제. 나중에 다시 풀어보기

def min_energy_to_sort(n, weights):
    # 정렬된 상태
    sorted_weights = sorted(weights)
    
    # 현재 위치를 저장하는 매핑
    index_map = {weight: i for i, weight in enumerate(sorted_weights)}
    
    # 방문 여부 체크
    visited = [False] * n
    min_energy = 0  # 최소 에너지 저장
    
    for i in range(n):
        # 이미 방문한 원소는 건너뜀
        if visited[i]:
            continue

        # 사이클을 찾기 위한 초기화
        cycle_sum = 0
        cycle_count = 0
        min_weight = float('inf')
        current = i

        while not visited[current]:
            visited[current] = True
            weight = weights[current]
            cycle_sum += weight
            min_weight = min(min_weight, weight)
            cycle_count += 1
            current = index_map[weight]  # 다음 위치로 이동

        # 사이클이 존재하는 경우, 최소 에너지 계산
        if cycle_count > 1:
            min_energy += min(
                cycle_sum + (cycle_count - 2) * min_weight,  # 기본 방식
                cycle_sum + min_weight + (cycle_count + 1) * sorted_weights[0]  # 전역 최소 사용 방식
            )

    return min_energy


# 입력 처리
n = int(input().strip())  # 추의 개수
weights = [int(input().strip()) for _ in range(n)]  # 추의 무게 리스트

# 결과 출력
print(min_energy_to_sort(n, weights))
