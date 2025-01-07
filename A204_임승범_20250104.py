# A204. 팩토리얼 0의 개수 - Baekjoon

N = int(input())

factorial = 1
for i in range(1, N+1):
    factorial *= i

str = str(factorial)

str_list = list(str)
str_list.reverse()

count = 0
for item in str_list:
    if item != '0':
        break
    else:
        count += 1

print(count)

# GPT 풀이: 팩토리얼의 끝 0의 개수는 5의 배수가 몇 번 곱해졌는지에 의해 결정됨.
# def count_trailing_zeros(n):
#     count = 0
#     while n >= 5:
#         count += n // 5
#         n //= 5
#     return count

# # 입력 받기
# n = int(input())

# # 결과 출력
# print(count_trailing_zeros(n))