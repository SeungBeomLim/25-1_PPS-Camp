# A201. 단어 뒤집기2 - Baekjoon

def reverse_words_in_string(S):
    result = []
    temp = []
    mode = 1  # 1: 일반 모드, 0: 태그 모드

    for char in S:
        if char == '<':
            if temp:
                result.append(''.join(temp[::-1]))  # 기존 temp에 있는 단어를 뒤집어 추가
                temp = []
            result.append(char)  # '<'를 결과에 추가
            mode = 0  # 태그 모드로 전환
        elif char == '>':
            result.append(char)  # '>'는 결과에 그대로 추가
            mode = 1  # 태그 종료, 일반 모드로 전환
        elif mode == 0:
            result.append(char)  # 태그 모드일 경우 그냥 그대로 추가
        else:
            if char == ' ':
                # 공백은 단어가 끝났다는 표시
                if temp:
                    result.append(''.join(temp[::-1]))  # temp에 있는 단어를 뒤집어서 결과에 추가
                    temp = []
                result.append(char)  # 공백도 결과에 추가
            else:
                temp.append(char)  # 일반 모드일 때는 단어를 temp에 추가

    # 마지막에 남아있는 단어 뒤집어서 추가
    if temp:
        result.append(''.join(temp[::-1]))

    return ''.join(result)


S = input()

# 결과 출력
print(reverse_words_in_string(S))
