class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        m = len(s)
        n = len(t)
        while j < n and i < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m
        