from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i]>0:
                break
        right=i
        left=i-1
        result=[]
        while right < len(nums) and left >= 0:
            if nums[right]**2<nums[left]**2:
                result.append(nums[right]**2)
                right+=1
            else:
                result.append(nums[left]**2)
                left-=1
        
        while right < len(nums):
            result.append(nums[right]**2)
            right+=1
        
        while left >=0:
            result.append(nums[left]**2)
            left-=1
        return result
            
                

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))