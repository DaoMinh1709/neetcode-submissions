class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        dp = [0] * n
        pfs = [0] * n
        stack = []  

        pfs[0] = height[0]
        stack.append(0)
        for i in range(1, n):
            pfs[i] = height[i] + pfs[i - 1]
            last = i - 1
            #print(i, ":")
            #print(stack)
            while stack and height[stack[-1]] <= height[i]:
                last = stack[-1]
                stack.pop()
            if stack: last = stack[-1]
            #print(stack, last)
            stack.append(i)
            dp[i] = dp[last] + min(height[i], height[last]) * (i - last - 1) - (pfs[i - 1] - pfs[last])
            #print(dp[i])
        #print(dp[n - 1])
        return dp[n - 1]
