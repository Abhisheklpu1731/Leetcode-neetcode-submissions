class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i in range(len(nums)):
            kn = target - nums[i]

            if kn in res:
                return [res[kn], i]

            res[nums[i]] = i

        return []