class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = [], []

        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        idx_pos, idx_neg = 0, 1
        for num_pos, num_neg in zip(positive, negative):
            nums[idx_pos] = num_pos
            nums[idx_neg] = num_neg
            idx_pos = idx_neg + 1 
            idx_neg += 2
        return nums