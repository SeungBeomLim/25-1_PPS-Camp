# B023. Kth Largest Element in a Stream - Leetcode
# heapq library에 대해서 공부해보기.

import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # 최소 힙으로 변환
        while len(self.min_heap) > k:  # k개까지만 유지
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)  # 새로운 값 추가
        if len(self.min_heap) > self.k:  # 힙 크기가 k 초과면 제거
            heapq.heappop(self.min_heap)
        return self.min_heap[0]  # k번째로 큰 값 반환
