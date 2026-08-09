class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums.sort()

        longest = 1
        count = 1

        for i in range(1, len(nums)):

            # skip duplicates
            if nums[i] == nums[i - 1]:
                continue

            # consecutive number
            elif nums[i] == nums[i - 1] + 1:
                count += 1

            # sequence broken
            else:
                longest = max(longest, count)
                count = 1

        # final update
        longest = max(longest, count)

        return longest