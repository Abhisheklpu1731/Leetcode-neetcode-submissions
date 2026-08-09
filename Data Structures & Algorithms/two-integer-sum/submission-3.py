class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff = {}

        for i in range(len(nums)):

            needed = target - nums[i]

            if needed in diff:
                return [diff[needed], i]

            diff[nums[i]] = i