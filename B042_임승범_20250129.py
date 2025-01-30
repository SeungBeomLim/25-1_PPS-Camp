# B042. Split a String in Balanced Strings - LeetCode

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = [0, 0]
        count = 0

        for char in s:
            if char == 'R':
                stack[0] += 1
            else:
                stack[1] += 1

            if stack[0] == stack[1]:
                stack[0], stack[1] = 0, 0
                count += 1
        
        return count