# A209. Base Conversion - Baekjoon

A, B = map(int, input().split()) # A진법, B진법
m = int(input()) # A진법 자릿 수
digits = list(map(int, input().split())) # A진법 숫자

# A진법 -> 10진법 변환
decimal_value = 0
for i in range(m):
    decimal_value = decimal_value * A + digits[i]

# 10진법 -> B진법 변환
result = []
while decimal_value > 0:
    result.append(decimal_value % B)
    decimal_value //= B

# unpacking 연산자 *를 이용해서 리스트를 공백으로 출력
print(*result[::-1])
