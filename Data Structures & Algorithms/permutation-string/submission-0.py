class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dic={}
        s2dic={}
        left=0
        right=left
        for i in range(len(s1)):
            s1dic[s1[i]]=1+s1dic.get(s1[i],0)

        for right in range(len(s2)):
            s2dic[s2[right]]=1+s2dic.get(s2[right],0)

            if (right-left+1)>len(s1):
                s2dic[s2[left]] -= 1

                if s2dic[s2[left]]==0:
                    del s2dic[s2[left]]
                left+=1

            #compareig s1dic and s2dic:
            if s1dic==s2dic:
                return True
            
        return False
            
        
        