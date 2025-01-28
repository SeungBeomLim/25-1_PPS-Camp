# B037. 방탈출 - Baekjoon

N = int(input())
target = list(map(int, input().split()))

current = [0] * N
count = 0
for i in range(N-2):
    if current[i] != target[i]:
        count += 1
        current[i] = 1 if current[i] == 0 else 0
        current[i+1] = 1 if current[i+1] == 0 else 0
        current[i+2] = 1 if current[i+2] == 0 else 0

if current[-2] != target[-2]:
    count += 1
    current[-1] = 1 if current[-1] == 0 else 0

if current[-1] != target[-1]:
    count += 1

print(count)