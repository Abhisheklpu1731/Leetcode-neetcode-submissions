class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        n = len(temperatures)

        i = 0
        while i < n:
            j = i + 1

            while j < n:
                if temperatures[j] > temperatures[i]:
                    ans.append(j - i)
                    break
                j += 1

            if j == n:
                ans.append(0)

            i += 1

        return ans