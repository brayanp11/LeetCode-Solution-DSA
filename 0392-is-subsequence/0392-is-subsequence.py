class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        slow, fast = 0, 0
        while fast < len(t) and slow < len(s):
            if s[slow] == t[fast]:
                slow += 1
            fast += 1
        return slow == len(s)