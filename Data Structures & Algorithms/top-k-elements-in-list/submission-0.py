class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for n in nums:
            cnt[n] = 1 + cnt.get(n, 0)
        arr = sorted(cnt.items(), key=lambda item: item[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(arr[i][0])
        return ans