class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i>=len(nums):
                res.append(list(subset))
                return

            #include case
            subset.append(nums[i])
            dfs(i+1)

            #remove case
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
        


