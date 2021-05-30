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
    def validPalindrome(self, word: str) -> bool:
        word = word.lower()
        word = [s for s in word if s.isalnum()]
        start, end = 0, len(word) -1
        while start <=end:
            if word[start]!=word[end]:
                return False
            start+=1
            end-=1
        return True
sol = Solution()
print(sol.validPalindrome("race a car"))
print(sol.validPalindrome("Tenet"))