class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mark = {}
        for str in strs:
            temp = "".join(sorted(str))
            mark.setdefault(temp, []).append(str)
        ans = [];
        for value in mark.values():
            ans.append(value)
        return ans

        