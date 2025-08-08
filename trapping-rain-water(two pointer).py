class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxl=0
        maxr=0
        res=0
        while(i<j):
            maxl=max(maxl,height[i])
            maxr=max(maxr,height[j])
            if maxl<maxr:
                
                res+=maxl-height[i]
                i+=1
            else:
                
                res+=maxr-height[j]
                j-=1
        return res

            
        