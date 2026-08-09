class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen=list()
        n=len(nums)
        for i in range(n):
            if nums[i] not in seen:
                seen.append(nums[i])
            elif nums[i] in seen:
                return True
        return False