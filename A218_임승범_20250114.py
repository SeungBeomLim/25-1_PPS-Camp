# A218. 할로윈의 사탕 - Baekjoon

T = int(input())

for _ in range(T):
    c, v = map(int, input().split())

    pieces_per_brother = c // v
    dad_gets = c % v
    
    print(f"You get {pieces_per_brother} piece(s) and your dad gets {dad_gets} piece(s).")
    
