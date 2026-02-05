
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()

        a = len(set(pattern))
        b = len(set(s))
        c = len(set(zip_longest(s,pattern)))

        return a == b and c == b



         


