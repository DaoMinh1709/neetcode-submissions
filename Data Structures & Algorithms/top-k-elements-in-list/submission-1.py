class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = defaultdict(list)
        ans = []
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for i, j in count.items():
            freq[j].append(i)
        for i in range(len(nums), 0, -1):
            if i in freq:
                k -= len(freq[i])
                ans.extend(freq[i])
            if k == 0: break
        return ans
