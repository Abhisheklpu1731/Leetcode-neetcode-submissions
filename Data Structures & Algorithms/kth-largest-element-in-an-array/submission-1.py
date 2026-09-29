class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for curr in nums:
            heapq.heappush(heap,curr)

            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]