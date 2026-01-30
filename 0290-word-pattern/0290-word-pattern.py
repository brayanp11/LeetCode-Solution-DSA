class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        maps = {}
        used_words = set()
        words = s.split()

        if len(pattern) != len(words):
            return False

        for char, word in zip(pattern, words):
            if char in maps:
                if maps[char] != word:
                    return False
            else:
                if word in used_words:
                    return False

                maps[char] = word
                used_words.add(word)
        return True

                