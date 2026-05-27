class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        for num in nums:
            if num not in h:
                h[num]=1
            h[num]+=1
            
        a=sorted(h,key=h.get,reverse=True)
        return a[:k]
        