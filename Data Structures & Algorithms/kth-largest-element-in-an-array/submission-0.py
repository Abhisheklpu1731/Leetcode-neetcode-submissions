class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [-x for x in nums]

        heapq.heapify(heap)

        for curr in range(k):
            maxi = -heapq.heappop(heap)

        return maxi