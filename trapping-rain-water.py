class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxleft=[0]*n
        maxright=[0]*n
        count=0
        for i in range(1,n):
            maxleft[i]=max(maxleft[i-1],height[i-1])
        for j in range(n-2,-1,-1):
            maxright[j]=max(maxright[j+1],height[j+1])
        for l in range(n):
            area=min(maxleft[l],maxright[l])-height[l]
            if area>0:
                count+=area
        return count