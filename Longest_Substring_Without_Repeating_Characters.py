class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString= {}
        start=max_length=0
        for i in range(len(s)):
            # print("index: "+str(i))
            # print("Start_bef = "+str(start))
            if s[i] in subString and start<=subString[s[i]]:
                start = subString[s[i]]+1
                sub=subString[s[i]]
                # print("SubString :"+str(sub))
                # print("Start :"+str(start))
            else:
                max_length=max(max_length, i-start+1)
            subString[s[i]] = i
            # print(subString)
        return max_length