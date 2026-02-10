class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[],[]]
        hashset1 = set(nums1)
        hashset2 = set(nums2)
        for num in nums2:
            if num not in hashset1 and num not in ans[1]:
                ans[1].append(num)

        for num in nums1:
            if num not in hashset2 and num not in ans[0]:
                ans[0].append(num)

        return ans