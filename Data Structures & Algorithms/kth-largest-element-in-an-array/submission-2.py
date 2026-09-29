class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq
        heapq.heapify_max(nums)
        for _ in range(k):
            result = heapq.heappop_max(nums)
        return result