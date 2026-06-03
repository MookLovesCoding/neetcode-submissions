class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]": "[", "}":"{"}
        for char in s:
            if char in closeToOpen:
                if stack and closeToOpen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False