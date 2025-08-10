class Solution:
    def palindromePairs(self, words):
        def is_palindrome(s):
            return s == s[::-1]       
        word_map = {word: i for i, word in enumerate(words)}
        result = []       
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back in word_map and word_map[back] != i:
                        result.append([word_map[back], i])
                if j != len(word) and is_palindrome(suffix):
                    front = prefix[::-1]
                    if front in word_map and word_map[front] != i:
                        result.append([i, word_map[front]])      
        return result
