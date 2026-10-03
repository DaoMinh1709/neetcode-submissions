class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mark = defaultdict(list)
        for str in strs:
            temp = "".join(sorted(str))
            mark[temp].append(str)

        return list(mark.values())

        