class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        n = len(s)
        while (i < n):
            j = s.find('#', i)
            l = int(s[i:j])
            i = j + 1
            ans.append(s[i:(i + l)])
            i += l
        return ans  
