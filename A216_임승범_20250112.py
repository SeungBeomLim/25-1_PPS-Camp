# A216. 집 주소 - Baekjoon

while True:
    num = int(input())
    if num == 0:
        break
    
    total = 0
    count = 0

    while num > 0:
        res = num % 10
        count += 1

        if res == 1:
            total += 2
        elif res == 0:
            total += 4
        else:
            total += 3

        num //= 10

    total += count - 1

    print(total + 2)
