class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # Create a table to store information about palindromic substrings
        table = [[False] * n for _ in range(n)]

        # All substrings of length 1 are palindromes
        for i in range(n):
            table[i][i] = True

        start = 0  # Initialize the start index of the longest palindromic substring
        max_length = 1  # Initialize the length of the longest palindromic substring

        # Check substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                max_length = 2

        # Check substrings of length 3 or more
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                # Check if the substring is a palindrome
                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] = True
                    start = i
                    max_length = k

        # Return the longest palindromic substring
        return s[start:start + max_length]