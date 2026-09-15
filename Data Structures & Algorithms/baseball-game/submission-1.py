class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation.lstrip("-").isdigit():
                stack.append(int(operation))
            elif operation == '+':
                prev1 = stack[-1]
                prev2 = stack[-2]
                stack.append(prev1 + prev2)
            elif operation == 'D':
                prev = stack[-1]
                stack.append(prev * 2)
            elif operation == 'C':
                stack.pop()

        return sum(stack)