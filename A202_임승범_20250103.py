# A202. 후위 표기식2 - Baekjoon

# 피연산자의 개수 입력
N = int(input())

# 후위 표기식 입력
expression = input()

# 각 피연산자의 값
values = [int(input()) for _ in range(N)]

stack = []
for char in expression:
    if char.isalpha():
        stack.append(values[ord(char) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()

        if char == '+':
            stack.append(a+b)
        elif char == '-':
            stack.append(a-b)
        elif char == '*':
            stack.append(a*b)
        elif char == '/':
            stack.append(a/b)

print(f"{stack[-1]:.2f}")