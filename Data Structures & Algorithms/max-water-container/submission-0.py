class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i=0
        j=n-1
        lenght=1
        height=1
        area=0
        maxi=0
        while i<j:
            lenght=j-i
            height=min(heights[i],heights[j])
            area=lenght*height
            maxi=max(maxi,area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxi
