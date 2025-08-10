class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(sub):
            return sub == sub[::-1]
        longest = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if is_palindrome(sub) and len(sub) > len(longest):
                    longest = sub
        return longest
