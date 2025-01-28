# B032. 이잠님 초대 - Baekjoon

N = int(input())
T = list(map(int, input().split()))

T.sort(reverse=True)

max_days = 0

for i in range(N):
    # 심는 데 걸린 날 + 나무 자라는 날
    max_days = max(max_days, i + 1 + T[i])

# 모든 나무가 다 자란 다음 날 이장님 초대
print(max_days + 1)
