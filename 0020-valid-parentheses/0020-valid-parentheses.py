class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c not in parentheses:
                stack.append(c)
            elif stack and stack[-1] == parentheses[c]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
