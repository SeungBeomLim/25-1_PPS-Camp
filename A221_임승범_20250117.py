# A221. 홀수일까 짝수일까 - Baekjoon

N = int(input())

for _ in range(N):
    print("odd" if int(input()) % 2 == 1 else "even")