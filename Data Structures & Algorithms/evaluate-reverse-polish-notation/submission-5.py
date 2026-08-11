class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'+', '-', '*', '/'}
        stack = []

        def applyOperand(operand: str, x: int, y: int) -> int:
            if operand == '+':
                return x + y
            elif operand == '-':
                return x - y
            elif operand == '*':
                return x * y
            elif operand == '/':
                return int(x/y)

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                res = applyOperand(token, x, y)
                stack.append(res)
        return stack[-1]