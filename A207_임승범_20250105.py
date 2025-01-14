# A207. 8진수 2진수 - Baekjoon

octal = input().strip()
list = list(map(int, str(octal)))

if octal == '0':
    print(0)
else:
    # 8진수를 10진수로 변환 후, 다시 2진수로 변환
    binary = bin(int(octal, 8))[2:]  # bin()의 결과 앞의 '0b' 제거
    print(binary)
    