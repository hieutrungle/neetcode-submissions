class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            if token not in '*/+-':
                stack.append(int(token))
                continue
            b = int(stack.pop())
            a = int(stack.pop())
            if token == "*":
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
            elif token == '+':
                stack.append(a + b)
            else:
                stack.append(a - b)
        return int(stack.pop())


    # 10 * (6 / ((9 + 3) * (-11))) + 17 + 5