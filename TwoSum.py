class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementComIndex = dict()
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if(num in complementComIndex):
                return [complementComIndex[num],i]
            else:
                complementComIndex[complement] = i;