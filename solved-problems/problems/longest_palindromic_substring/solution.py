class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for cl in range(2,n + 1):
            for i in range(n - cl + 1):
                j = i + cl -1 
                if(s[i] == s[j] and cl == 2):
                    dp[i][j] = 1
                elif(s[i] == s[j]):
                    dp[i][j] = dp[i+1][j-1]


        max_len = 0
        start = 0
        for i in range(n):
            for j in range(n):
                if(dp[i][j] and max_len < j - i + 1):
                    max_len = j - i + 1
                    start = i

        return s[start:start + max_len]

