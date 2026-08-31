class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj={}
        for num in nums:
            maj[num]=maj.get(num,0)+1
        return max(maj, key=maj.get)
        