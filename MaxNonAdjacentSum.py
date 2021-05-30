
class Solution:
  def find_max_sum(self,arr):
    incl = 0
    excl = 0
    
    for i in arr:
      
      # Current max excluding i (No ternary in
      # Python)
      new_excl = excl if excl>incl else incl
      
      # Current max including i
      incl = excl + i
      excl = new_excl
    
    # return max of incl and excl
    return (excl if excl>incl else incl)

sol = Solution()
print(sol.find_max_sum([5,5,1,1]))