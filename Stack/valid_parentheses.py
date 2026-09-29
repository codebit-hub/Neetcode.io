class Solution:
    def isValid(self, s: str) -> bool:
        slovarb = {"}": "{", "]": "[", ")": "("}
        stack = []
        for c in s:
            if c in slovarb.values():
                stack.append(c)
            elif c in slovarb.keys():
                if not stack:
                    return False
                node = stack.pop()
                if node != slovarb[c]:
                    return False
            else:
                return False
        return len(stack) == 0
