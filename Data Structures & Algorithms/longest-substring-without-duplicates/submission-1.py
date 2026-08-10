class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = set()
        left = 0
        maxlen = 0

        for right in range(len(s)):

            while s[right] in s1:
                s1.remove(s[left])
                left += 1

            s1.add(s[right])

            maxlen = max(maxlen, right - left + 1)

        return maxlen