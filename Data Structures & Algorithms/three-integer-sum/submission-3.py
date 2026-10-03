class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        mark = set()
        ans = []
        for i in range(n):
            target = 0 - nums[i]
            l, r = i + 1, n - 1
            while (l < r):
                total = nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    if not tuple((nums[i], nums[l], nums[r])) in mark:    
                        ans.append([nums[i], nums[l], nums[r]])
                        mark.add(tuple((nums[i], nums[l], nums[r])))
                    l += 1
        return ans
                