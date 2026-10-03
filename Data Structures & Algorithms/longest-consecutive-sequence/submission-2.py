class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        ans = 0

        for i in nums:
            if not mp[i]:
                mp[i] = mp[i - 1] + mp[i + 1] + 1
                mp[i - mp[i - 1]] = mp[i]
                mp[i + mp[i + 1]] = mp[i]
                ans = max(ans, mp[i])

        return ans
