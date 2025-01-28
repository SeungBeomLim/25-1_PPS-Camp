# B029. Array Partition - Leetcode
# https://leetcode.com/problems/array-partition/description/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        return sum(nums[::2])