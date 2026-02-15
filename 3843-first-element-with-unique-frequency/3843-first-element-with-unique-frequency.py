from collections import Counter

class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:

        freq = Counter(nums)
        freq_value = Counter(freq.values())
        for num in nums:
            if freq_value[freq[num]] == 1:
                return num
        return -1