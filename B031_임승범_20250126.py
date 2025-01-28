# B031. 라디오 - Baekjoon

A, B = map(int, input().split())
N = int(input())

frequency = []

for _ in range(N):
    frequency.append(int(input()))

min_value = 99999
count = 0
for i in range(N):
    min_value = min(min_value, abs(B - frequency[i]))

if min_value == 0:
    count = 1
elif min_value >= abs(B-A):
    count = abs(B-A)
else:
    count = 1 + abs(min_value)

print(count)

# GPT 풀이
A, B = map(int, input().split())
N = int(input())

# 즐겨찾기 주파수 입력 받기
presets = [int(input()) for _ in range(N)]

# 직접 +1/-1 버튼만 사용하는 경우
direct = abs(B - A)

# 즐겨찾기 버튼을 사용한 경우
preset_presses = [abs(B - p) + 1 for p in presets]

# 최소 버튼 클릭 수 계산
min_clicks = min([direct] + preset_presses)

# 결과 출력
print(min_clicks)
