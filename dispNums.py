from typing import List
class Solution:
    def findDisappear(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            new_index=abs(nums[i])-1
            if nums[new_index]>0:
                nums[new_index]*=-1
        result=[]
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(i+1)
        return result
sol = Solution()
print(sol.findDisappear([4,3,2,7,8,2,3,1]))