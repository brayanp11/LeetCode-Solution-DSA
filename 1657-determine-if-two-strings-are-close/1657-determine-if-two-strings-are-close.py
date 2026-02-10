class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        count1, count2 = defaultdict(int), defaultdict(int)
        for i in range(len(word1)):
            count1[word1[i]] += 1
            count2[word2[i]] += 1

        if set(count1.keys()) != set(count2.keys()):
            return False

        return sorted(count1.values()) == sorted(count2.values())