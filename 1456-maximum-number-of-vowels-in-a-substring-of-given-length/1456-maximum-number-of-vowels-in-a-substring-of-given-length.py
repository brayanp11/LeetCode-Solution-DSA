class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_vowels = curr_vowels = sum(1 for c in s[:k] if c in vowels)
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr_vowels += 1
            if s[i - k] in vowels:
                curr_vowels -= 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels