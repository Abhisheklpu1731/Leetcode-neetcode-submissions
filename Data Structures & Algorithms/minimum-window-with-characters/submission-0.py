class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Frequency of characters required from t
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        # Frequency of characters currently in the window
        countS = {}

        left = 0
        have = 0
        need = len(countT)

        min_len = float("inf")
        result = ""

        for right in range(len(s)):

            # Add right character to window
            char = s[right]
            countS[char] = countS.get(char, 0) + 1

            # This character has now satisfied its required frequency
            if char in countT and countS[char] == countT[char]:
                have += 1

            # Window contains everything we need
            while have == need:

                # Check if current window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                # Remove left character
                left_char = s[left]
                countS[left_char] -= 1

                # We just lost a required character
                if left_char in countT and countS[left_char] < countT[left_char]:
                    have -= 1

                left += 1

        return result