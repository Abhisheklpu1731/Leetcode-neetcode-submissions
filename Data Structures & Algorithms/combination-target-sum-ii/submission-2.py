class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        total=0
        
        candidates.sort()
        def dfs(i,total):
            if total==target:
                res.append(list(subset))
                return
            if i>=len(candidates) or total>target:
                return   
            #inclduing case:
            subset.append(candidates[i])
            dfs(i+1,total+candidates[i])

            # Exclude current element
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            #exlcuding case:
            subset.pop()
            dfs(i+1,total)

        dfs(0,0)
        return res


            
        