class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        """if len(s) <= 0:
            return True"""

        slow, fast = 0, 0
        while fast < len(t) and slow < len(s):
            if fast < len(t) and s[slow] != t[fast]:
                fast += 1
            elif fast < len(t) and s[slow] == t[fast]:
                slow += 1
                fast += 1
        return slow == len(s)