# Input = "race a car"
# Output = False

# Input = "Tenet"
# Output = True

'''
Approach:
1. Compare string and reversed string -> O(n) space
2. 2 pointer at both ends moving towards the center -> O(1) space
'''

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:\
        pass
sol = Solution()
print(sol.twoSum([2,7,11,15],9))