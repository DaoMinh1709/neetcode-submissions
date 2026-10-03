class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) + 1
        prfL = [1] * (n + 1)
        prfR = [1] * (n + 1)
        for i in range(1, n):
            prfL[i] = nums[i - 1] * prfL[i - 1]
        for i in range(n - 1, 0, -1):
            prfR[i] = nums[i - 1] * prfR[i + 1]
        
        res = []
        for i in range(1, n):
            res.append(prfL[i - 1] * prfR[i + 1])
        return res
        