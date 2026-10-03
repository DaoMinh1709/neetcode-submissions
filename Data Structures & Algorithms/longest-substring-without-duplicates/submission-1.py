class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        id = [-1] * 128
        res, cnt, last = 0, 0, 0
        for i in range(len(s)):
            val = ord(s[i])
            if id[val] == -1 or id[val] < last:
                cnt += 1
            else:
                cnt = i - id[val]
                last = id[val] + 1
    
            id[val] = i
            res = max(res, cnt)
        return res
                