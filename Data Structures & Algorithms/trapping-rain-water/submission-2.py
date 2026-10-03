class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pref = [0] * n
        suff = [0] * n
        for i in range(1, n):
            pref[i] = max(height[i - 1], pref[i - 1])
        for i in range(n - 2, -1, - 1):
            suff[i] = max(height[i + 1], suff[i + 1])
        res = 0
        for i in range(n):
            res += max(0, min(pref[i], suff[i]) - height[i])
        return res
