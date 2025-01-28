# B036. 잃어버린 괄호 - Baekjoon

# -를 기준으로 split
expression = input().split('-')

# 앞에 +부분 더하기
total = sum(map(int, expression[0].split('+')))

# 뒤에 더한 후 앞에꺼에서 빼기
for part in expression[1:]:
    total -= sum(map(int, part.split('+')))

print(total)