# B083. 스네이크버드 - Baekjoon

N, L = map(int, input().split())
fruits = list(map(int, input().split()))

fruits.sort()

for fruit in fruits:
    if L >= fruit:
        L += 1

print(L)