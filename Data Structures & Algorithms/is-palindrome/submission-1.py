class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i=0
        j=n-1
        s=s.lower()
        while i<j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True



            