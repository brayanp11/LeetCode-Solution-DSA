class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zerocount = 0
        left = 0
        lenwindow = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zerocount += 1

            while zerocount > k:
                if nums[left] == 0:
                    zerocount -= 1
                left += 1

            lenwindow = max(lenwindow, right - left + 1)
        
        return lenwindow