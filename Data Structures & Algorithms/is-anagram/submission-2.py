class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram of each other or not
        S=len(s)
        T=len(s)
        Se={}
        Te={}
        for se in s:
            if se in Se:
                Se[se]+=1
            else:
                Se[se]=1
        for te in t:
            if te in Te:
                Te[te]+=1
            else:
                Te[te]=1
        return Te==Se


        