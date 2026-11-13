class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
            else:
                if len(st) == 0 or st[-1] != self.opp(c): 
                    return False;
                st.pop()
        return len(st) == 0

    def opp(self, c: char) -> char:
        if (c == ')'): return '('
        if (c == ']'): return '['
        if (c == '}'): return '{'
