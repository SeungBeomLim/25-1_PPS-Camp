# A212. 동물원 - Baekjoon


# 1번 풀이: https://great-park.tistory.com/131
# 새로운 2*1 우리가 추가 되었을 때, 1) 사자를 추가, 2) 사자를 추가하지 않음으로 점화식을 세운 경우.

N = int(input())

if N == 1:
    print(3)
else:
    dp = [1 for _ in range(N+1)]
    dp[1], dp[2] = 3, 7

    for i in range(3, N+1):
        dp[i] = (2 * dp[i-1] + dp[i-2]) % 9901

    print(dp[N])

# 2번 풀이: GPT
# 2*N 배열에서 배치할 수 있는 모든 경우의 수를 dp에서 누적으로 계산

N = int(input())

dp = [[0] * 3 for _ in range(N+1)]
dp[1][0] = 1 # 사자 배치 X
dp[1][1] = 1 # 사자 왼쪽 배치
dp[1][2] = 1 # 사자 오른쪽 배치

for i in range(2, N+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

print((dp[N][0] + dp[N][1] + dp[N][2]) % 9901)