class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mark = {}
        for n in nums:
            mark[n] = 1
        start = []
        for n in nums:
            if n - 1 not in mark:
                start.append(n)
        
        ans = 0
        for n in start:
            cur = n
            cnt = 1
            while cur + 1 in mark:
                cnt += 1
                cur += 1
            ans = max(ans, cnt)
        
        return ans

