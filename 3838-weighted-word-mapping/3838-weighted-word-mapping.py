class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result_chars = []

        for word in words:
            total_weight = 0
            for char in word:
                index_char = ord(char) - 97
                total_weight += weights[index_char]

            remainder = total_weight % 26

            mapped_char = chr(122 - remainder)

            result_chars.append(mapped_char)

        return "".join(result_chars)