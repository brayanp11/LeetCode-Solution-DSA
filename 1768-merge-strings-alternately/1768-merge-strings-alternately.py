class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        for char1, char2 in zip(word1, word2):
            res.append(char1)
            res.append(char2)

        if len(word1) > len(word2):
            end = [char for char in word1[len(word2):]]
            return "".join(res + end)
        else:
            end = [char for char in word2[len(word1):]]
            return "".join(res + end)