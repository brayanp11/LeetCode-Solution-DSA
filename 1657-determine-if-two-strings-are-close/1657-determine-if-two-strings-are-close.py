class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        setword1, setword2 = set(word1), set(word2)

        count1, count2 = defaultdict(int), defaultdict(int)
        for i in range(len(word1)):
            count1[word1[i]] += 1
            count2[word2[i]] += 1
            if word1[i] not in setword2 or word2[i] not in setword1:
                return False

        

        return sorted(list(count1.values())) == sorted(list(count2.values()))