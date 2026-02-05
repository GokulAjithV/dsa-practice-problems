class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        char_index = {}  # Dictionary to store the index of characters
        max_length = 0
        start = 0  # Starting index of the current substring

        for end in range(n):
            if s[end] in char_index and char_index[s[end]] >= start:
                # If the character is already in the current substring, update the starting index
                start = char_index[s[end]] + 1
            char_index[s[end]] = end  # Update the index of the character
            max_length = max(max_length, end - start + 1)

        return max_length