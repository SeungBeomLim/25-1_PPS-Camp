# B043. Happy Number - LeetCode

# 1번 풀이
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        elif n < 10:
            return False
        else:
            sum = 0
            while n > 0:
                temp = n % 10
                sum += temp**2
                n = n // 10
            
            return self.isHappy(sum)
        

# 2번 풀이
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # 이전에 등장한 숫자 저장
        
        while n != 1 and n not in seen:
            seen.add(n)  # 현재 숫자 기록
            n = sum(int(digit) ** 2 for digit in str(n))  # 각 자리 숫자의 제곱합 계산
        
        return n == 1  # 1이면 True, 아니면 False