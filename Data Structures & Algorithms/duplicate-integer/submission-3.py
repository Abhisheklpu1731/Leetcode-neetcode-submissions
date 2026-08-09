class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        '''for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                if nums[i] == nums[j]:
                    return True

        return False'''
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for k,v in d.items():
            if v>=2:
                return True
        return False