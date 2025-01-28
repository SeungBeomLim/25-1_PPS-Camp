# B030. Maximize Sum Of Array After K Negations - Leetcode

# Easy Solution
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for _ in range(k):
            smallest = min(nums)
            smallest_idx = nums.index(smallest)
            nums[smallest_idx] = -smallest
        return sum(nums)
    

# Time Complexity를 고려한 Solution
import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(k):
            smallest = heapq.heappop(nums)
            heapq.heappush(nums, -smallest)
            
        return sum(nums)


