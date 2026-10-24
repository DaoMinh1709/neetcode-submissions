class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        countS = {}
        countT = {}
        need = len(t)
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        l = 0
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if countS.get(s[r], 0) <= countT.get(s[r], 0):
                need -= 1

            while need == 0:
                if (r - l + 1 < len(res)) or (res == ""):
                    res = s[l:r + 1]

                countS[s[l]] -= 1
                if countS[s[l]] < countT.get(s[l], 0):
                    need += 1
                l += 1
        return res