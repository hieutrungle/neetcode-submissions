class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if not stack and  c in ')}]':
                return False
            if stack and ((stack[-1] == '[' and c == ']') or
                    (stack[-1] == '{' and c == '}') or
                    (stack[-1] == '(' and c == ')')):
                    stack.pop()
                    continue
            stack.append(c)

        return True if not stack else False