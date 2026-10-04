class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        id = defaultdict(list)
        res = min(len(s), k + 1)
        
        for i in range(len(s)):
            id[s[i]].append(i)

        for arr in id.values():
            #print(arr)
            l, r, n = 0, 0, len(arr)
            while r < n - 1:
                remain = k - ((arr[r + 1] - arr[l] + 1) - (r + 1 - l + 1))
                if remain >= 0:
                    #print("valid")
                    r += 1
                else: 
                    l += 1
                    r += 1
                #print(l, r, arr[l], arr[r])
                res = max(res, arr[r] - arr[l] + 1 + min(arr[l] + len(s) - arr[r] - 1, remain))
        return res
