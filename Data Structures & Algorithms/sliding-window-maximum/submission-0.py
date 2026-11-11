class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        res = []
        for i in range(len(nums)):
            while len(dq) != 0 and nums[dq[-1]] <= nums[i]:
                dq.pop()
            while len(dq) != 0 and dq[0] <= i - k:
                dq.popleft()
            dq.append(i);
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res