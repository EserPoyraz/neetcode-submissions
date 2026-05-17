class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = [None] *(len(nums)*2)

        for i in range(len(nums)*2):
        
            if(i<len(nums)):
                ans[i] = nums[i]
            else:
                concateI = i - len(nums)
                ans[i] = nums[concateI]
        
        return ans 
        