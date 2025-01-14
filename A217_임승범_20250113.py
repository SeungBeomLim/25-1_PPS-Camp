# A217. 암호 - Baekjoon

plain_text = input()
key = input()

result = []
key_length = len(key)

for i in range(len(plain_text)):
    char = plain_text[i]

    if 'a' <= char <= 'z':
        key_char = key[i % key_length]
        encrypted_char = chr(((ord(char) - ord(key_char) - 1) % 26) + ord('a'))

        result.append(encrypted_char)
    else:
        result.append(char)

print(''.join(result))