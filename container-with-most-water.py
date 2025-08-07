class Solution:
    def maxArea(self, height: List[int]) -> int:
        max1=0
        i=0
        j=len(height)-1
        while(i<j):
            area=min(height[i],height[j])*(j-i)
            max1=max(area,max1)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max1