# A205. 조합 0의 개수 - Baekjoon

def count_factors(n, factor):
    """
    n!에서 특정 factor(2 또는 5)의 개수를 구하는 함수.
    5의 배수, 25의 배수, 125의 배수 등을 고려하여 반복적으로 몫을 더함.
    """
    count = 0
    while n >= factor:
        count += n // factor
        n //= factor
    return count

def trailing_zeros_in_combination(n, m):
    """
    조합 nCm의 끝자리 0의 개수를 구하는 함수.
    끝자리 0은 2와 5의 쌍에 의해 결정되며,
    5의 개수가 항상 2의 개수보다 적으므로 5의 개수로 판단.
    """
    # nCm = n! / (m! * (n-m)!)
    # 따라서 끝자리 0의 개수 = (n!의 5의 개수) - (m!의 5의 개수) - ((n-m)!의 5의 개수)
    five_count = count_factors(n, 5) - count_factors(m, 5) - count_factors(n - m, 5)
    two_count = count_factors(n, 2) - count_factors(m, 2) - count_factors(n - m, 2)
    
    # 끝자리 0의 개수는 5와 2의 쌍 중 최소값
    return min(five_count, two_count)

# 입력 처리
n, m = map(int, input().split())  # n과 m을 입력받음

# 결과 출력
print(trailing_zeros_in_combination(n, m))
