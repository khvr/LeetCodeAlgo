# Input = ["h","e","l","l","o"]
# Output = ["o","l","l","e","h"]

# Input = "Tenet"
# Output = True

'''
Approach:
1. 2 pointer at both ends moving towards the center -> O(1) space
'''

from typing import List
class Solution:
    def reverseString(self, strList: List[int]) -> List[int]:
        start,end = 0,len(strList)-1
        while start<=end:
            strList[start],strList[end]=strList[end],strList[start]
            start+=1
            end-=1
        return strList
sol = Solution()
print(sol.reverseString(["h","e","l","l","o"]))
