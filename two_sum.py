class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash={}
        for i in range(len(nums)):
            hash[nums[i]]=i
        for j in range(len(nums)):
            diff=target-nums[j]
            if diff in hash and hash[diff]!=j:
                return [j , hash[diff]]
        

        

