class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')':'(', '}':'{', ']':'['}
        stacky = []

        for char in s:
            if char not in close_to_open:
                stacky.append(char)
            elif char in close_to_open and stacky and stacky[-1] == close_to_open[char]:
                stacky.pop()
            elif char in close_to_open and ((stacky and stacky[-1] != close_to_open[char]) or not stacky):
                return False

        return False if stacky else True 